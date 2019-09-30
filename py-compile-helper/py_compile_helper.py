#!/usr/bin/python3.7

import argparse
import py_compile
import os
import subprocess
import shutil

args = None


def resolve_args():
    parser = argparse.ArgumentParser(description='A helper for recursive compilation of python modules')
    parser.add_argument('input', help="input folder that must be compiled")
    parser.add_argument('output', help="output folder to save compiled files")
    parser.add_argument('-o', '--optimize', type=int, default=2,
                        help="optimization level: -1,0,1,2 for py_compile.compile() ")
    parser.add_argument('-i', '--include', action="store_true", help="include the compilation of tests")
    parser.add_argument('-z', '--zip', action="store_true", help="add compiled files to zip archive")
    parser.add_argument('-c', '--clean', action="store_true", help="cleans cache by py3clean in the source folder")

    global args
    args = parser.parse_args()

    if not args.input.endswith("/"):
        args.input += "/"
    if not args.output.endswith("/"):
        args.output += "/"

    if not args.include:
        print("The compilation of the test modules will be skipped. Use -i flag to include tests in case of necessity.")
    print("Input location: %s, output location: %s" % (args.input, args.output))
    print("Compile optimization level: %s\n" % args.optimize)


def compile_single(input_name, output_name):
    print("compile: ", input_name, "--->", output_name)
    py_compile.compile(input_name, output_name, optimize=args.optimize)


def get_module_name(path):
    module_name = path.split("/")[-1]
    if not module_name:
        module_name = "root"
    return module_name


def skip_module(module_name, root):
    is_test = "test" in module_name or "test" in root
    return is_test and not args.include


def iterate_over_folders():
    for root, dirs, files in os.walk(args.input):
        if any(".py" in s for s in files):
            module_name = get_module_name(root)
            print("\nModule: %s, files: %s (%s)" % (module_name, len(files), root.replace(args.input, '')))
            if not skip_module(module_name, root):
                iterate_over_files(root, files)
            else:
                print("skipped")


def iterate_over_files(root, files):
    for f in files:
        file_path = os.path.join(root, f)
        if f.endswith(".py"):
            output = file_path.replace(args.input, args.output) + "c"
            compile_single(file_path, output)


def clean_cache():
    if args.clean:
        subprocess.call(["py3clean", args.input])


def create_zip():
    if args.zip:
        file_path = args.output + "../python-compiled"
        dir_to_zip = args.output
        print("\nAdding compiled files to zip archive: %s" % file_path)
        shutil.make_archive(file_path, 'zip', dir_to_zip)


if __name__ == '__main__':
    resolve_args()
    clean_cache()
    iterate_over_folders()
    create_zip()
