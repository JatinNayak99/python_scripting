# swap the value of two variables without using any other variables

a = int(input("A = "))
b = int(input("B = "))

a = a + b
b = a - b
a = a - b

print("A =",a)
print("B =",b)