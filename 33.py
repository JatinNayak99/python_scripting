# get one number and perform factorial

n = int(input("N = "))

a = 1
for i in range (1,n+1):
    a = a * i

print("Factorial =",a)