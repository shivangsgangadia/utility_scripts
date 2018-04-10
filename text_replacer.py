#it's python bro.....
import os
import argparse

p = argparse.ArgumentParser()
p.add_argument("text", help = "text to be replaced", type=str)
p.add_argument("replacement",help = "replacement text", type=str)
p.add_argument("dir",help = "directory where files are stored", type=str)
args = p.parse_args()

text = args.text
replacement = args.replacement
directory = args.dir

text_length = len(text)
replacement_length = len(replacement)

for filename in os.listdir(directory):
	filename = "./test/"+filename
	f = open(filename, "r")
	original = f.read()
	newstr = ""
	f.close()
	f = open(filename, "w")
	original_length = len(original)
	i = 0
	while( i < original_length):
		if original[i]==text[0]:
			o_str = original[i:(i+text_length)]
			if o_str==text:
				for item in replacement:
					newstr += item
				i += text_length - 1
			else:
				newstr += original[i]
		else:
			newstr += original[i]
		i+=1
	f.write(newstr)
	f.close()
