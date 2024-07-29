# Check whether a given number is a 3-digit number or not

num = int(input("Enter a number: "))

count = 0

while num:
    num = num // 10
    count += 1

print("Yes 3-digit no" if count >= 3 else "Not a 3-digit no")