# Calculate the sum of digits of given number using while loop

Num = int(input("Enter a number: "))
sum = 0

while Num:
    rem = Num % 10
    sum += rem
    Num //= 10

print(sum)