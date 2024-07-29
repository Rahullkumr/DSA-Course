# Check a 3-digit number is Armstrong or not
# abc = a^3 + b^3 + c^3 = abc ==> Armstrong
# Eg: 153, 370, 371


def is_armstrong(num):
    copy, sum = num, 0
    while num:
        rem = num % 10
        sum += rem**3
        num //= 10
    return True if copy == sum else False


print("Yes, Armstrong" if is_armstrong(123) else "Not Armstrong")