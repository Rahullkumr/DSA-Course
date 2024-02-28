# reverse digits

def reverse_digits(num):
    reversed_no = 0
    while num:
        rem = num % 10
        reversed_no = reversed_no * 10 + rem
        num //= 10
    return reversed_no

print(reverse_digits(1936328))
# ---------------------------------------------

# You are given an integer N and the task is to reverse the digits of the given integer. 
# Return 0 if the result overflows and does not fit in a 32 bit signed integer

# Input:  123
# output: 321

# Input: -123
# output: -321

# Input: 9999999123
# output: 0


def reverse_it(A):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    if A < 0:
        if (-int(str(A)[::-1].rstrip('-'))) < INT_MIN:
            return 0
        return -int(str(A)[::-1].rstrip('-'))			
    else:
        if int(str(A)[::-1]) > INT_MAX:
            return 0
        return int(str(A)[::-1])

print(reverse_it(123))
print(reverse_it(-123))
