# remove last digit from a given number

num = int(input("Enter a number greater than 2 digit: "))

if -10 < num < 10:
    print(num)
else:
    print(num//10)