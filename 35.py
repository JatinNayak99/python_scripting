# get one number and check if it is armstrong or not

num = n = int(input("N = "))
l = len(str(n))
sum = 0
while n != 0:
    a = n % 10
    sum = sum + (a ** l)
    n = n // 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")