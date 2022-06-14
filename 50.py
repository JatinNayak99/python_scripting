'''
get one number and print:
-------------------------
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''

n = int(input("N = "))
for i in range (1,n+1):
    for j in range (i,0,-1):
        print(j,end=" ")
    print()