'''
get one number and print:
-------------------------
A B C D E
B C D E
C D E
D E
E
'''

n = int(input("N = "))

for i in range (n,0,-1):
    for j in range (0,i):
        print(end=chr(ord('A')+j+(n-i))+" ")
    print()