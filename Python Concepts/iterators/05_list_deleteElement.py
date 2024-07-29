# WAPS to print a new array deleting a specific element

arr = [2*n for n in range(1,11)] # list comprehension

print(arr)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
del arr[2]  # deleting element 6
print(arr)  # [2, 4, 8, 10, 12, 14, 16, 18, 20]