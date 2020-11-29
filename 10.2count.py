#taking filename from user
filename = input("Enter a file name: ")
#opening the given file
file = open(filename, "r")
#reading file data into a string
f = file.read()
end = 0
counts = {}
#loop runs until we can't find "From" substring
while(f.find("From",end) != -1):
    #finding starting and ending indexs of line
    start = f.find("From",end)
    end = f.find("\n",start)
    #splitting the data in the line
    line = f[start:end].split()
    #getting mail in the line
    mail = line[1]
    #update count in dict if already there
    if(mail in counts):
        counts[mail] += 1
    #create new key(mail) with value = 1
    else:
        counts[mail] = 1

#converting dictionory to list of tuples
clist = []
for mail,count in counts.items():
    clist.append((count, mail))
#sorting list in reverse
clist.sort(reverse=True)
#printing the first tuple data (mail with max count)
print(clist[0][1],clist[0][0])