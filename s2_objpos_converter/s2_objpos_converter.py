#!/usr/bin/python3.7

import argparse
import os
import sys
import zipfile
from pathlib import Path
import ntpath
import csv

args = None

UE4_MULTIPLIER = 3.048

def resolve_args():
    parser = argparse.ArgumentParser(description='Converter of the s2 .objpos files into UE4 format')
    parser.add_argument('-s', '--single', help="path of the one selected .s2z or .objpos file")
    parser.add_argument('-f', '--folder', help="path of the directory with the .s2z or .objpos files")
    parser.add_argument('-o', '--output', type=str, default='./ut4',
                        help="output folder to save converted files; default location: new directory './ut4'")

    global args
    args = parser.parse_args()

    if not (args.single or args.folder):
        sys.exit('At least one of two parameters must be specified: -s or -f. Use --help for additional info.')

    if args.folder:
        args.folder += "/"
    if args.output:
        args.output += "/"

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    if args.single:
        print(f'Input location: {args.single}, output location: {args.output}')
    else:
        print(f'Input location: {args.folder}, output location: {args.output}')


def init_files_list(path_single, path_folder):
    target = Target()

    if path_single and path_single.lower().endswith(".objpos"):
        target.plain_text_file_paths.add(path_single)
    elif path_single and path_single.lower().endswith(".s2z"):
        target.archives_file_paths.add(path_single)
    else:
        for root, dirs, files in os.walk(path_folder):
            for f in files:
                file_path = os.path.join(root, f)
                if f.lower().endswith(".objpos"):
                    target.plain_text_file_paths.add(file_path)
                if f.lower().endswith(".s2z"):
                    target.archives_file_paths.add(file_path)

    target.print()
    return target


class Target:
    def __init__(self):
        self.plain_text_file_paths = set()
        self.archives_file_paths = set()
        self.s2_maps = {}

    def init_s2_maps(self):
        for file in self.plain_text_file_paths:
            s2_obj_pos = S2ObjPos()
            with open(file) as f:
                unfiltered = [c.strip() for c in f.readlines()]
            for u in unfiltered:
                s2_obj_pos.add_positions(u)
            self.s2_maps[Path(f.name).stem] = s2_obj_pos

        for archive in self.archives_file_paths:
            s2_obj_pos = S2ObjPos()
            with zipfile.ZipFile(archive, 'r') as s2z:
                with s2z.open(Target._get_s2z_inner_obj_pos_path(archive)) as f:
                    unfiltered = [c.strip() for c in f.readlines()]
                    for u in unfiltered:
                        s2_obj_pos.add_binary_positions(u)
            self.s2_maps[Path(f.name).stem] = s2_obj_pos

    def print(self):
        print(f'Found plain text: {self.plain_text_file_paths}')
        print(f'Found archives: {self.plain_text_file_paths}')

    @staticmethod
    def _get_s2z_inner_obj_pos_path(path):
        head, tail = ntpath.split(path)
        file_name = os.path.splitext(tail or ntpath.basename(head))[0]
        return f'world/{file_name}/{file_name}.objpos'

    def __str__(self):
        return f'plain text: {self.plain_text_file_paths}, archives: {self.archives_file_paths}'


def create_object(s: str):
    if S2Object.PREFIX in s:
        return S2Object(s)
    elif S2Reference.PREFIX in s:
        return S2Reference(s)
    else:
        return None


def write_csv(target: Target):
    for k, v in target.s2_maps.items():
        print(f'{k}  --->  {args.output}{k}.csv')

        rows_counter = 0
        with open(f'{args.output}{k}.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = [
                '',
                'class',
                'object',
                'posX',
                'posY',
                'posZ',
                'rotX',
                'rotY',
                'rotZ',
                'scale'
            ]

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for obj in v.s2_object_positions:
                writer.writerow(
                    {
                        '': rows_counter,
                        'class': obj.prefix,
                        'object': obj.name,
                        'posX': obj.x * UE4_MULTIPLIER,
                        'posY': obj.y * UE4_MULTIPLIER,
                        'posZ': obj.z * UE4_MULTIPLIER,
                        'rotX': obj.a,
                        'rotY': obj.b,
                        'rotZ': obj.c,
                        'scale': obj.d,
                    })
                rows_counter = rows_counter + 1


class S2ObjPos:
    def __init__(self):
        self.s2_object_positions = list()

    def add_positions(self, line: str):
        s2_object = create_object(line)
        if s2_object:
            self.s2_object_positions.append(s2_object)

    def add_binary_positions(self, binary_line):
        s2_object = create_object(binary_line.decode('utf-8'))
        if s2_object:
            self.s2_object_positions.append(s2_object)


class S2Object:
    # ex.: createObject mossrock 5956.0 2808.0 41.0 158.0 1.272 0.0 0.0  <-- [8]
    PREFIX = 'createObject'

    def __init__(self, s: str):
        self.line = s.strip().lower()
        p = self.line.split()
        self.prefix = S2Object.PREFIX
        self.name = p[1]
        self.x = float(p[2])
        self.y = float(p[3])
        self.z = float(p[4])
        self.a = float(p[5])
        self.b = float(p[6])
        self.c = float(p[7])
        self.d = float(p[8])

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {}'.format(
            self.prefix,
            self.name,
            self.x,
            self.y,
            self.z,
            self.a,
            self.b,
            self.c,
            self.d)


class S2Reference:
    # ex.: createReference npc_kongor 1292.0 6688.0 996.0 209.0 1.520 0.0 0.0  <-- [8]
    PREFIX = 'createReference'

    def __init__(self, s: str):
        self.prefix = S2Reference.PREFIX
        self.line = s.strip().lower()
        p = self.line.split()
        self.name = p[1]
        self.x = float(p[2])
        self.y = float(p[3])
        self.z = float(p[4])
        self.a = float(p[5])
        self.b = float(p[6])
        self.c = float(p[7])
        self.d = float(p[8])

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {}'.format(
            self.prefix,
            self.name,
            self.x,
            self.y,
            self.z,
            self.a,
            self.b,
            self.c,
            self.d)


if __name__ == '__main__':
    resolve_args()
    t = init_files_list(args.single, args.folder)
    t.init_s2_maps()
    write_csv(t)
