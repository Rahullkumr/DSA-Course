# check whether a given number is prime or not

num = int(input("Enter a positive number: "))

i = 2
while i < num:
    if num % i == 0:
        print("Not a prime number")
        break
    i += 1
else:
    print("Prime number")



