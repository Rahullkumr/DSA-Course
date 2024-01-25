# Swap data of two variables

var1, var2 = input("Enter data for var1: "), input("Enter data for var2: ")

print("Before swap: \n",var1, var2)

var1, var2 = var2, var1

print(f"After swap: \n {var1} {var2}")