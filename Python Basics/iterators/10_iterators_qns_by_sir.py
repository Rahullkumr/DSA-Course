'''
1. WAPS to sort a tuple of tuples by the second item:
    tuple1 = (('a',21), ('b', 37), ('c',11), ('d', 29))

2. WAPS to reverse a given string word by word

3. WAPS to create a list of first N prime numbers where N is given by user.

4. WAPS to convert a list of strings into a dictionary where keys are first 
    alphabet of the strings and data corresponding to the keys are lists of strings 
    started from that alphabet.
'''
# Solution

def qn_one():
    # chatGPT answer
    def get_second_element(item):
        return item[1]

    tuple1 = (('a',21), ('b', 37), ('c',11), ('d', 29))
    print(tuple1)

    sorted_tuple = sorted(tuple1, key=get_second_element)
    print(sorted_tuple)


def qn_two(text):
    text = text.strip(' ')
    words = text.split(' ')[::-1]
    reverse_text = ' '.join(words)

    print(reverse_text)

def qn_three(N):
    if N <= 1:
        print("Not prime")

    def is_prime(num):
        is_prime_or_not = True
        for i in range(2, num):
            if num % i == 0:
                is_prime_or_not = False
        return is_prime_or_not

    for i in range(2, N + 1):
        if is_prime(i):
            print(i)

def qn_four(list_of_str):
    print(list_of_str)
    dict_of_str = {}
    for element in list_of_str:
        key, value = element[0], element
        dict_of_str[key] = value
    print(dict_of_str)
        


qn_one()
print()
qn_two("This is a car")
print()
qn_three(int(input('Enter N: ')))
print()
qn_four(['apple', 'fan', 'color', 'bird', 'laughter', 'jacket'])