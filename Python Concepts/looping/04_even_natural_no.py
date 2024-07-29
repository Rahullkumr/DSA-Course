# print first N even Natural numbers using while loop

N = int(input("Enter N: "))
i = 1
while i <= N:
    if i % 2 == 0:
        print(i)
    i += 1