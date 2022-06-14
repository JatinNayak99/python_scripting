'''
get one number and print:
-------------------------
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''

n = int(input("N = "))

for i in range (n,0,-1):
    for j in range (i,n+1):
        if j % 2 == 0:
            print(end="0 ")
        else:
            print(end="1 ")
    print()