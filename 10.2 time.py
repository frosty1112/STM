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
    #splitting time
    time = line[5].split(":")
    #finding hour value
    hour = time[0]
    #update count in dict if already there
    if(hour in counts):
        counts[hour] += 1
    #create new key(hour) with value = 1
    else:
        counts[hour] = 1
        
#printing the hours and count
for hour,count in counts.items():
    print(hour,count)