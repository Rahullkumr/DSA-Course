import threading

even, odd = [], []

def find():
    for i in range(30, 51):
        if i % 2 == 0:
            global even
            even.append(i)
        else:
            global odd
            odd.append(i)

def printw():
    global even
    for i in even:
        print(i, end=" ")
    
    global odd
    for j in odd:
        print(j, end=" ")

t1 = threading.Thread(target=find)
t2 = threading.Thread(target=printw)

t1.start()
t2.start()

t1.join()
t2.join()

print("Execution done")
