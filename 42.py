'''
get one number and print:
-------------------------
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''

n = int(input("N = "))
for i in range (1,n+1):
    print(end=" "*(n-i))
    print("* "*i)
for i in range (n-1,0,-1):
    print(end=" "*(n-i))
    print("* "*i)