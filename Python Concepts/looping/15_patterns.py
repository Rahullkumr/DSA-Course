# print the given patterns in optimised time

for i in range(1, 6):
    print(" * " * i)

print()

for i in range(5, 0, -1):
    print(" * " * i)

print()

space = 4
for i in range(1, 6):
    print("   " * space, " * " * i)
    space -= 1 