# Calculate LCM of two given numbers using while loop
# LCM * HCF = num1 * num2

def LCM_byMe(num1, num2):
    bigger = num1 if num1 > num2 else num2
    i = 1
    while True:
        multiple = bigger * i
        if multiple % num1 == 0 and multiple % num2 == 0:
            print(f'LCM by me = {multiple}')
            break
        i += 1

# LCM optimised wrt time complexity for INTERVIEWBIT
def LCM_optimised(a, b):
    def hcf(a, b):
        while b:
            a, b = b, a % b
        return a

    print(f'Optimized LCM = {(a * b) // hcf(a, b)}')

num1, num2 = int(input("Enter first number: ")), int(input("Enter second number: "))

LCM_byMe(num1, num2)
LCM_optimised(num1, num2)
