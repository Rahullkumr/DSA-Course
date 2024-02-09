# Find maximum and minimum elements in an array

arr = [3,5,6,2,0,8,9,1,6, 3, 0, 3, 5]

# using inbuilt functions
print("Using inbuilt functions: ")
print("Minimum = ", min(arr))
print("Maximum = ", max(arr))

# without using inbuilt functions
max_num = arr[0]
min_num = arr[0]
for i in arr:
    if i > max_num:
        max_num = i

    if i < min_num:
        min_num = i

print("Without using inbuilt functions: ")
print("Max = ",max_num)
print("Min = ",min_num)