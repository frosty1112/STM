numbers = []

while True:
    try:
        number = input("Enter a number: ")
        if number == "done":
            break
        number = int(number)
        numbers.append(number)
    except ValueError:
        print("Invalid input")


print(sum(numbers), len(numbers), sum(numbers)/len(numbers))
