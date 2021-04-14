#Takes files from ldd and copies them into a folder named data
import argparse
import os
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("file_name", help = "Name of executable", type=str)
s = p.parse_args()

file_name = s.file_name

def get_path(line):
    if '=>' in line:
        path = line.split(' => ')[1].split(' (')[0]
    else:
        path = line.split(' (')[0]
    return path.strip()
command = "ldd "+file_name+" > files.txt"
os.system(command)

f = open("files.txt","r")
os.system("mkdir data")
for line in f:
    source_file = get_path(line)
    print("Path: " + source_file)
    directory = Path("data" + str(Path(source_file).parent.absolute()))
    directory.mkdir(parents=True, exist_ok=True)
    print("Parent: " + str(directory))
    comm = "cp " + source_file + " " + str(directory)
    print(comm)
    os.system(comm)
    print("--------------------------")

f.close()
print("Done!")
