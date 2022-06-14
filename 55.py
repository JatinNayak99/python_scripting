'''
get one number and print:
-------------------------
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''

n = int(input("N = "))
for i in range (n,0,-1):
    print((str(i)+" ")*i)