# Check a number to be Palindrome or not

def reverse_digits(num):
    reversed_no = 0
    while num:
        rem = num % 10
        reversed_no = reversed_no * 10 + rem
        num //= 10
    return reversed_no


original = 123215
reverse = reverse_digits(original)
print("Palindrome" if original == reverse else "Not Palindrome")