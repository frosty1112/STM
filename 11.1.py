import re
pattern=input ("Enter a regular expression: ")
file=open ('mbox.txt')
count=0
#For each line
for line in file:
    line=line.rstrip()
    #It it meets the pattern
    if re.search (pattern, line) :
        #Add to count
        count+=1
print (('mbox.txt had %d that matched %s') % (count, pattern))