'''
    Docstring
'''


def sumit(till):
    '''A recursive fn to sum till n'''
    if till == 0:
        return 1
    else:
        return till + sumit(till - 1)

print(f"Sum till 5 using recursion: {sumit(5)}")
