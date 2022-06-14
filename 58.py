'''
get one number and print:
-------------------------
1 2 3 4 5
2 4 6 8
3 6 9
4 8
5
'''

n = int(input("N = "))
for i in range (n,0,-1):
    for j in range (1,i+1):
        print((n-i+1)*j,end=" ")
    print()