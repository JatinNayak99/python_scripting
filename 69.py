'''
get one number and print:
-------------------------
A B C D E
A B C D
A B C
A B
A
'''

n = int(input("N = "))

for i in range (n,0,-1):
    for j in range (0,i):
        print(end=chr(ord('A')+j)+" ")
    print()