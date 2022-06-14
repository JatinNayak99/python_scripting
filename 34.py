# get one number and check if it is prime or not

n = int(input("N = "))

a = 0
for i in range (2,n // 2):
    if n % i == 0:
        a = 1
        break
if a == 0:
    print("Prime Number")
else:
    print("Not Prime Number")