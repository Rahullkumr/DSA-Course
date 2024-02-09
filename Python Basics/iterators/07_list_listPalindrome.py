# Check if a given list/array is palindrome or not

even = [2, 4, 6, 8, 10, 8, 6, 4, 2]
print("Original: ",even)
print("Reversed: ",even[::-1])

print("Yes, Palindrome" if even == even[::-1] else "Not Palindrome")
