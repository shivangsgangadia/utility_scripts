#Takes files from ldd and copies them into a folder named data
import argparse
import os
from subprocess import call
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

call(["ldd",file_name,"> files.txt"])

f = open("files.txt","r")
call(["mkdir", "data"])
for line in f:
	source_file = get_path(line)
	new_file = "./data"
	call(["cp",source_file,new_file])

f.close()
print("Done!")
