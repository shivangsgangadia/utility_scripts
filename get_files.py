#Takes files from ldd and copies them into a folder named data
import argparse
import os

p = argparse.ArgumentParser()
p.add_argument("file_name", help = "Name of executable", type=str)
s = p.parse_args()

file_name = s.file_name

def get_path(line):
	i = 0
	l = len(line)
	ans = ""
	while(i<l):
		if(line[i]=='/'):
			j=i
			while(line[j]!=' '):
				j+=1
			ans = line[i:j]
			break
		i+=1
	return ans
command = "ldd "+file_name+" > files.txt"
os.system(command)

f = open("files.txt","r")
os.system("mkdir data")
for line in f:
	source_file = get_path(line)
	new_file = "./data"
	comm = "cp "+source_file+" "+new_file
	os.system(comm)

f.close()
print("Done!")
