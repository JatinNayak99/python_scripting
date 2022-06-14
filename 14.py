# get three number and find maximum among them

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

if a > b and a > c:
    print("A is MAX")
elif b > a and b > c:
    print("B is MAX")
else:
    print("C is MAX")