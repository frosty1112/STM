fname = input("Enter file name: ")
#open file in read mode
file = open(fname,"r")

#read 1st line
line=file.readline()

#read line by line and print in upper case
while line:
    print(line.upper())
    line = file.readline()

file.close()