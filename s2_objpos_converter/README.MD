## S2_OBJPOS_CONVERTER

Converter of the S2's `*.objpos` files into a CSV format for exporting into UE4

**Features**
- Can convert directly one `*.objpos` file
- Can convert directly one `*.s2z` file (`map.s2z` archive always has one `map.objpos` file inside: `map.s2z/world/map/map.objpos`)
- Can convert all files from the selected folder

**Output CSV format**
- converted `posX`, `posY`, `posZ` values are being multiplied by `3.048`
```
class,object,posX,posY,posZ,rotX,rotY,rotZ,scale
```

**Examples (Windows 10 x64):**
Running from a command-line (don't forget to install the latest python and add it into the path during the installation)
```
X:\Code\s2_objpos_converter>python s2_objpos_converter.py -f ./world

Input location: ./world/, output location: ./ut4/
Found plain text: {'./world/choke_fixed.objpos'}
Found archives: {'./world/eden2.s2z', './world/haven.s2z', './world/bunker.s2z'}
choke_fixed  --->  ./ut4/choke_fixed.csv
eden2  --->  ./ut4/eden2.csv
haven  --->  ./ut4/haven.csv
bunker  --->  ./ut4/bunker.csv
```


**Examples (Ubuntu x64):**

Listing --help information:
```
$ python3 ./s2_objpos_converter.py --help

usage: s2_objpos_converter.py [-h] [-s SINGLE] [-f FOLDER] [-o OUTPUT]

Converter of the s2 .objpos files into UE4 format

optional arguments:
  -h, --help            show this help message and exit
  -s SINGLE, --single SINGLE path of the one selected .s2z or .objpos file
  -f FOLDER, --folder FOLDER path of the directory with the .s2z or .objpos files
  -o OUTPUT, --output OUTPUT output folder to save converted files; default location: new directory './ut4'
```

Launching without any arguments:
```
$ python3 ./s2_objpos_converter.py
          At least one of two parameters must be specified: -s or -f. Use --help for additional info.
```

Launching with arguments
```
$ python3 ./s2_objpos_converter.py -f ./world
          Input location: ./world/, output location: ./ut4/
          Found plain text: {'./world/choke_fixed.objpos'}
          Found archives: {'./world/haven.s2z', './world/bunker.s2z', './world/eden2.s2z'}
          choke_fixed  --->  ./ut4/choke_fixed.csv
          haven  --->  ./ut4/haven.csv
          bunker  --->  ./ut4/bunker.csv
          eden2  --->  ./ut4/eden2.csv
```

Single file `s2z`
```
$ python3 ./s2_objpos_converter.py -s ./world/eden2.s2z
          Input location: ./world/eden2.s2z, output location: ./ut4/
          Found plain text: set()
          Found archives: {'./world/eden2.s2z'}
          eden2  --->  ./ut4/eden2.csv
```

Single file `objpos`
```
python3 ./s2_objpos_converter.py -s ./world/choke_fixed.objpos
          Input location: ./world/choke_fixed.objpos, output location: ./ut4/
          Found plain text: {'./world/choke_fixed.objpos'}
          Found archives: set()
          choke_fixed  --->  ./ut4/choke_fixed.csv
```

Custom folder
```
python3 ./s2_objpos_converter.py -s ./world/eden2.s2z -o ./custom_folder
          Input location: ./world/eden2.s2z, output location: ./custom_folder/
          Found plain text: set()
          Found archives: {'./world/eden2.s2z'}
          eden2  --->  ./custom_folder/eden2.csv
```

Output example `./ut4/choke_fixed.csv`
```


class,object,posX,posY,posZ,rotX,rotY,rotZ,scale
createReference,command_center,4605.528,1929.384,106.68,339.0,0.75,0.0,0.0
createReference,command_center,24832.056,26703.528000000002,188.976,174.0,0.75,0.0,0.0
createObject,ruins_tower,22296.12,23417.784,158.496,213.0,1.0,0.0,0.0
createObject,ruins_tower,6973.8240000000005,4919.472,12.192,40.0,0.912,0.0,0.0
createReference,redstone_mine,25938.48,25331.928,192.024,143.0,0.35,0.0,0.0
createReference,redstone_mine,3300.984,2947.416,88.392,132.0,0.33,0.0,0.0
createObject,snowtunnel,14764.512,13606.272,115.824,345.0,1.833,0.0,0.0
createObject,pinetree,14871.192000000001,4379.976,329.184,48.0,0.306,0.0,0.0
createObject,snowpinetree3,15581.376,3072.384,1039.368,186.0,0.583,0.0,0.0
createObject,full_tree,17571.72,6662.928,57.912,50.0,1.135,0.0,0.0
createObject,snowpinetree3,12643.104,20930.616,91.44,158.0,0.801,0.0,0.0
createObject,snowpinetree2,14813.28,23097.744,298.704,287.0,0.443,0.0,0.0
```