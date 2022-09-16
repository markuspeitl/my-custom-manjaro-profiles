import argparse
from os import path
import os

#Example:
#python3 package-module-compositor.py -s pkglists -a True -o result/test

#dirname = path.dirname(path.abspath(__file__))

parser = argparse.ArgumentParser(
    description="Consume package collection lists and stitch them together"
)

parser.add_argument('-s', '--source', help="Path of the directory from which to load package modules from")
parser.add_argument('-a', '--loadall', type=bool, default="False", help="Load all modules of a directory")
parser.add_argument('-i', '--input', nargs='+', help="Names of the modules from the pkglists directory to be consumed.")
parser.add_argument('-o', '--output', help="Output path for the resulting package file")

# Parse the arguments
arguments = parser.parse_args()

# Finally print the passed string

modules_dir="pkglists/"
if(arguments.source is not None):
    modules_dir=arguments.source

inputmodules = arguments.input
outpath = arguments.output

print("Input: " + str(inputmodules))
print("outpath: " + str(outpath))
if outpath==None:
    print("outpath is none - exitting")
    exit(1)

#outpath = "result/" + outpath

def mergeFiles(paths):
    mergedString=""

    for path in paths:
        with open(path, "r") as module_file:
            modules_contents = module_file.read()
            print(modules_contents)
            mergedString = mergedString + modules_contents + "\n\n"

    return mergedString;

with open(outpath, "w+") as out_file:


    modulePaths = []
    mergedResult=""

    if(arguments.loadall):
        
        files = os.listdir(modules_dir)
        for file in files:
            filepath = path.join(modules_dir, file)
            if os.path.isfile(filepath):
                print("Foundfile " + str(file))
                modulePaths.append(filepath)

    else:
        for inputmodule in inputmodules:
            #modulePath = path.join(dirname, modules_dir, inputmodule + ".txt")
            modulePath = path.join(modules_dir, inputmodule + ".txt")
            modulePaths.append(modulePath)
        
    mergedResult = mergeFiles(modulePaths)
    out_file.write(mergedResult)
