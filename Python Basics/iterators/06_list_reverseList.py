# WAPS to reverse a list

even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(even[::-1]) # list slicing

# whitout using list slicing
for i in range(len(even) - 1, -1, -1):
    print(even[i], end=" ")