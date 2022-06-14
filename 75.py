# get string and check if it is palindrome or not

n = str(input("S = ")).lower()
b = ""
for i in range (len(n)-1,-1,-1):
    b = b + n[i]

if n == b:
    print("String is palindrome")
else:
    print("String is not palindrome")