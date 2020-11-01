hrs = input("Enter Hours: ")

h = float(hrs)

b = input("Enter Rate: ")

basic = float(b)

if h <=40:

    payment = h * basic

elif h > 40:

    payment = 40* basic + (h-40)*1.5*basic

print ('Pay: ', payment)