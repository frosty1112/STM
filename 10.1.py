# taking filename from user
filename = input("Enter a file name: ")
# openng the given file
file = open(filename, "r")
# dictionary to count the number of messages
counts = {}

# loop inputs one line at a time from the file
# so we can process one line at a time instead
# of the whole file as one string.   
for line in file:              
    line = line.split() # splits the line with " " and stores it as a list
    if line[0] == "From":   # if the first item of the list is "From"
        mail = line[1]      # then get the mail, which is second item in the list.
      
    if mail in counts: # if mail already present in dictionry   
        counts[mail] +=1# then increment it's value by 1
    else:               # else if not present
        counts[mail] = 1# create key in dictionary and initialize value of 1
      
# converting dictionary to list of tuples
clist = []
for mail,count in counts.items():
    clist.append((count,mail))
# sorting list in reverse
clist.sort(reverse=True)
# printing the first tuple data (mail with max count)
print(clist[0][1],clist[0][0])