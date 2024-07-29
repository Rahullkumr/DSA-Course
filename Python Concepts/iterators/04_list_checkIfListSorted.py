# Check if given array is sorted

arr = [3,5,6,2,0,8,9,1,6, 3, 0, 3, 5]
li = [e*e for e in range(5)]    # list comprehension [0, 1, 4, 9, 16]

print(arr)
print("Yes, sorted" if arr == sorted(arr) else "Not sorted")
print(li)
print("Yes, sorted" if li == sorted(li) else "Not sorted")
