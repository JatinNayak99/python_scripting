# create function to find max from two numbers

def find_max (a,b):
    if a > b:
        return a
    else:
        return b

a = int(input("A = "))
b = int(input("B = "))
print("MAX =",find_max(a,b))