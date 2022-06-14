'''
get one number and print:
-------------------------
A A A A A
B B B B
C C C
D D
E
'''

n = int(input("N = "))

for i in range (0,n):
    print((chr(ord('A')+i)+" ")*(n-i))