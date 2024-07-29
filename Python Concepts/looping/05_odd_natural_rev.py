# print first 10 odd natural numbers in reverse order using while loop

N = 20
i = N

while i >= 1:
    if i % 2 == 1:
        print(i)
    i -= 1