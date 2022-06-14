'''
get one number and print:
-------------------------
2   4   6   8   10
4   6   8   10
6   8   10
8   10
10
'''

n = int(input("N = "))
for i in range (n,0,-1):
    for j in range (1,i+1):
        print(((n-i)*2)+(j*2),end=" ")
    print()