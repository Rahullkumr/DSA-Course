# GCD or HCF

def hcf(a,b):
# a,b = b, a % b
    while b:
    #    a = b
    #    b = a % b
       a,b = b, a % b
       print(a)
       print(b)
       print()
    return a

print(hcf(12,8))