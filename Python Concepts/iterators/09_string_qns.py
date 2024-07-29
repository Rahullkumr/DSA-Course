'''
You are given a string A of size N.
Print the string A after reversing the string word by word.

NOTE:
- A sequence of non-space characters constitutes a word.
- Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
- If there are multiple spaces between words, reduce them to a single space in the reversed string.
'''

def solve(A):
    B = A.strip()
    rev_list = B.split()[::-1]
    rev_str = ''
    for word in rev_list:
        rev_str += word
        rev_str += ' '
    print(rev_str.strip())

def solve_my_way(A):
    B = A.strip()
    rev_list = B.split()[::-1]
    rev_str = ' '.join(rev_list)
    print(rev_str.strip())

def solve_most_concise_way(A):
    print(' '.join(A.strip().split(' ')[::-1]))

solve_my_way("The sky is blue")
solve("The sky is blue")
solve_most_concise_way("The sky is blue    ")