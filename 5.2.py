from sys import maxsize
min = maxsize
max = -1
while True:
    # prompt for the input
    inp = input ('Enter a number : ')
    #if the input is done, break the loop
    if inp == 'done':
        break
        #making sure the entered input is valid
        try:
            if int (inp)<min:
                min = int(inp)
            if int (inp)>max:
                max = int(inp)
        except:
            print('Invalid input')

print('max : '+str(max)+' min : '+str(min))
