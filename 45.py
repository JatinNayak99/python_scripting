'''
get one number and print:
-------------------------
1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25
'''

n = int(input("N = "))
for i in range (1,n+1):
    a = 0
    for j in range (0,n):
        a = a + i
        print(a,end="\t")
    print()