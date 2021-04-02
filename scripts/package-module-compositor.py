import argparse
from os import path

modules_dir="pkglists/"
dirname = path.dirname(path.abspath(__file__))

parser = argparse.ArgumentParser(
    description="Consume package collection lists and stitch them together"
)

parser.add_argument('-i', '--input', nargs='+', help="Names of the modules from the pkglists directory to be consumed.")
parser.add_argument('-o', '--output', help="Output path for the resulting package file")

# Parse the arguments
arguments = parser.parse_args()

# Finally print the passed string

inputmodules = arguments.input
outpath = arguments.output

print("Input: " + str(inputmodules))
print("outpath: " + str(outpath))
if outpath==None:
    print("outpath is none - exitting")
    exit(1)

outpath = "result/" + outpath

with open(outpath, "w+") as out_file:

    for inputmodule in inputmodules:
        modulePath = path.join(dirname, modules_dir, inputmodule + ".txt")

        with open(modulePath, "r") as module_file:
            modules_contents = module_file.read()
            print(modules_contents)
            out_file.write(modules_contents + "\n\n")
