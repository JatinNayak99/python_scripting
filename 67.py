'''
get one number and print:
-------------------------
Z
Y X
W V U
T S R Q
P O N M L
'''

n = int(input("N = "))
a = ord('Z')
for i in range (0,n):
    for j in range (0,i+1):
        print(end=chr(a)+" ")
        a = a - 1
    print()