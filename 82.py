# create function to calculate power of given number

def power (n,p):
    x = 1
    for i in range (0,p):
        x = x * n
    return x

n = int(input("N = "))
p = int(input("P = "))
print("Power =",power(n,p))