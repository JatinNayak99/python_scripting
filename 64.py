'''
get one number and print:
-------------------------
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
'''

n = int(input("N = "))
for i in range (0,n):
    print((chr(ord('A')+i)+" ")*n)