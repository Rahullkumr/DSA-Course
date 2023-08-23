'''
    fibo: 0 1 1 2 3 5 8 13
    indx: 0 1 2 3 4 5 6 7
'''
def fibo(nth_pos):
    '''A fn to return fibonaci no at nth position'''
    fib_nos = [0, 1]
    first, second, third = 0, 1, 0
    
    third = first + second
    fib_nos.append(third)

    for i in range(11):
        first = second
        second = third
        third = first + second
        fib_nos.append(third)
    return fib_nos[nth_pos - 1]

print(f"Fibonaci no at 6th position: {fibo(6)}")
