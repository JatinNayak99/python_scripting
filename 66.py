'''
get one number and print:
-------------------------
A
B C
D E F
G H I J
K L M N O
'''

n = int(input("N = "))
a = 0
for i in range (0,n):
    for j in range (0,i+1):
        print(end=(chr(ord('A')+a)+" "))
        a = a + 1
    print()