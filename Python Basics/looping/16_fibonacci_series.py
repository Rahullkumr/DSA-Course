# Print fibonacci series upto given limit


first =  1
second = 2
limit = int(input("How many fibonacci numbers do you want: ")) - 2
print(first, second, end=" ")

while limit:
    third = first + second
    first, second = second, third
    limit -= 1
    print(third, end=" ")
print()