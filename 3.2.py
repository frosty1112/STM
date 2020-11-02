try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    if hours <= 40:
        print("Pay:", hours * rate)
    else:
        print("Pay:", 40 * rate + (hours - 40) * 1.5 * rate)
except ValueError:
    print("Error, please enter numeric input")