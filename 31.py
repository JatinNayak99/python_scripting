# get one number and display in reverse

n = int(input("N = "))

# b = 0
# while n != 0:
#     a = n % 10
#     b = b * 10 + a
#     n = n // 10

c = ""
while n != 0:
    c = c + str(n % 10)
    n = n // 10

print("Reverse =",c)