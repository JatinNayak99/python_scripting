# get one number and print fibonacci series (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...)

n = int(input("N = "))
a = 0
t = b = 1
print(a,"",end="")
for i in range (0,n):
    print(t,end=" ")
    t = a + b
    a = b
    b = t