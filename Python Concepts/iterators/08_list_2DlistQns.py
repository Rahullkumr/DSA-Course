# 2D array / list 

arr = [
        [e for e in range(5)],
        [2*e for e in range(5)],
        [2*e-1 for e in range(1,6)],
        [e*e for e in range(1,6)],
        [e**3 for e in range(1,6)]
    ]

# Generted using list comprehension
# [[0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [1, 4, 9, 16, 25], [1, 8, 27, 64, 125]]

# Print the list in 2D form
def print_2d():
    # [
    #   [0, 1, 2, 3, 4], 
    #   [0, 2, 4, 6, 8], 
    #   [1, 3, 5, 7, 9], 
    #   [1, 4, 9, 16, 25], 
    #   [1, 8, 27, 64, 125]
    # ]

    for i in range(5):
        for j in range(5):
            print(arr[i][j], end=" ")
        print()

# search an element in a 2D list
def search_element(find):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == find:
                print(f'Found at row {i + 1} column {j + 1}')
                return 
    print("Not present")

# sum and average of all elements in a 2D list
def sum_average():
    sum = 0
    for i in range(5):
        for j in range(5):
            sum += arr[i][j]

    print("Sum = ",sum)
    print("Average = ", sum/25)

# find sum of both diagonal elements in a 2D list
def sum_of_diagonal():
    sum = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                sum += arr[i][j]
    print("Sum = ",sum)


is_true = True
print()
print(arr)
while is_true:
    print()
    choice = int(input("1. Print list in 2D format\n2. Search an element\n3. Sum and average\n4. Sum of diagonal elements\n5. Enter 5 to exit\n\n"))
    
    match choice:
        case 1:
            print_2d()
        case 2:
            search_me = int(input("Enter a number to find: "))
            search_element(search_me)
        case 3:
            sum_average()
        case 4:
            sum_of_diagonal()
        case 5:
            is_true = False
        case _:
            print("Enter valid number\n")
