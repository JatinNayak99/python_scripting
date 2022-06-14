'''
get one number and print:
-------------------------
A
B B
C C C
D D D D
E E E E E
'''

n = int(input("N = "))
for i in range (1,n+1):
    print((chr(ord('A')+i-1)+" ")*i)