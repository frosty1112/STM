#function to print lines in file in caps
def file2caps():
                #reading file name
                filename=input("Enter file name :: ");
                #opening the data file
                file=open(filename,'r')
                #loop to read each line
                for line in file:
                                #printing the line in uppercase
                                print(line.upper(),end='')
                                #end of loop
                #end of function
#calling the function
file2caps();
