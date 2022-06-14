'''
get one number and print:
-------------------------
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
'''

n = int(input("N = "))
for i in range (n,0,-1):
    for j in range (1,i+1):
        print(n-i+j,end=" ")
    print()