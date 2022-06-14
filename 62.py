'''
get one number and print:
-------------------------
1   2   3   4   5   5   4   3   2   1
1   2   3   4           4   3   2   1
1   2   3                   3   2   1
1   2                           2   1
1                                   1
'''

n = int(input("N = "))
for i in range (n,0,-1):
    for j in range (1,i+1):
        print(j,end=" ")
    print(end="    "*(n-i))
    for j in range (i,0,-1):
        print(j,end=" ")
    print()