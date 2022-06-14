# create function to find fectorial of given number using recursion

def fectorial (n):
    if n == 1:
        return n
    else:
        return n*fectorial(n-1)

n = int(input("N = "))
print("Fectorial =",fectorial(n))