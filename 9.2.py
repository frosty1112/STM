import os
import string

file_name = input("Enter File_Name: ")
path = os.path.join(os.getcwd(),file_name)
day_dict = {}

with open (path) as fin:
    for line in fin:
        line = fin.readline()
  
if (line.startswith("from") or line.startswith("From") and len(line)>3):
    words = line.split(" ")
day = words[2]
day_dict[day] = day_dict.get(day,0)+1
print(day_dict)