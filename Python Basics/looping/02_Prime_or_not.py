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



# Other way

'''
def is_prime(no):
    if no == 2:
        return True 

    for i in range(2, no):
        return False if (no % i == 0) else True
        

print("yes" if is_prime(2) else "no")
'''
