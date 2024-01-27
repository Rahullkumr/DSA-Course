# Count digits in a given number using while loop

Num = int(input("Enter a number: "))
count = 0

while Num:
    Num = Num // 10
    count += 1

print(count)