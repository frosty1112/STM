def computepay(hour, rate):
    if hour <=40:
            return hour*rate

    return 40*rate + (hour-rate)*1.5*rate



h = int(input("Enter hours: "))
r = float(input("Enter rate: "))
print("Pay:",computepay(h,r))
