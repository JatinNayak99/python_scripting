'''
get one number and print:
-------------------------
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''

n = int(input("N = "))
for i in range (n,0,-1):
    for j in range (0,i):
        print(n-j,end=" ")
    print()