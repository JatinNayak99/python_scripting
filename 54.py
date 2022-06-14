'''
get one number and print:
-------------------------
1
1 0
1 0 1
1 0 1 0
1 0 1 0 1
'''

n = int(input("N = "))
for i in range (0,n):
    for j in range (0,i+1):
        if j % 2 == 0:
            print(end="1 ")
        else:
            print(end="0 ")
    print()