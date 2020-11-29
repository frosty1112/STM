#file name input
name = input("Enter file:")
fh = open(name)

#dict mails ids and count
master = dict()

#reading through the file and store mail id and count in master
for lines in fh:
    if not 'From ' in lines:
        continue
    else:
        recipient = lines.split()
        emails = recipient[1]
        master[emails] = master.get(emails, 0) + 1

#print master

print(master)