'''
get one number and print:
-------------------------
1
1 0
1 0 0
1 0 0 0
1 0 0 0 0
'''

n = int(input("N = "))
for i in range (0,n):
    print(end="1 ")
    print("0 "*i)
