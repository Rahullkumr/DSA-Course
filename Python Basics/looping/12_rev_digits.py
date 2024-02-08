# reverse digits

def reverse_digits(num):
    reversed_no = 0
    while num:
        rem = num % 10
        reversed_no = reversed_no * 10 + rem
        num //= 10
    return reversed_no

print(reverse_digits(1936328))