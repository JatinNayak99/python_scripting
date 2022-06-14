# create function to find average of given numbers

def average (*n):
    total = 0
    for i in n:
        total = total + i
    return total / len(n)
n1 = int(input("N1 = "))
n2 = int(input("N2 = "))
n3 = int(input("N3 = "))
print("Average =",average(n1,n2,n3))