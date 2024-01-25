# Check whether a number is positive, negative or zero

num = int(input("Enter a number: "))

if num == 0:
    print("Zero")
else:
    print("Positive" if num > 0 else "Negative")