inp = input('Enter Celsius Temperature:')
try:
    cel = float(inp) 
    fahr = (cel + 32.0) * 9.0 / 5.0
    print(fahr)
except:
    print('Please enter a number')