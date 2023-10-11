def check_factors(n):
    for factor in range(2, n):
        if n % factor == 0:
            factors_list.append(factor)

def check_prime(no):
    if no == 2:
        return True
    for i in range(2,no):
        if no % i == 0:
            return False
    return True
    

num = int(input("Enter number to get prime factors: "))

factors_list = []
prime_factors_list = []
if num in (0,1):
    print("Enter greater number")
elif num < 0:
    print("Enter positive number")
elif num == 2:
    print(num)
else:
    check_factors(num)
    print(f"Factors: {factors_list}")

for i in factors_list:
    if check_prime(i):
        prime_factors_list.append(i)

print(f"Prime factors of {num} : {prime_factors_list}")