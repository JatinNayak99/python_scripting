# get one number and perform sum of digit of that number

n = int(input("N = "))

sum = 0
while n != 0:
    a = n % 10
    sum = sum + a
    n = n // 10

print("Reverse =",sum)