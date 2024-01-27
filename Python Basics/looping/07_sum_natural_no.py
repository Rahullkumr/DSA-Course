# calculate sum of first N natural numbers using while loop

N = int(input("Enter N: "))
sum, i = 0, 1

while i <= N:
    sum += i
    i += 1

print(f'Sum = {sum}')