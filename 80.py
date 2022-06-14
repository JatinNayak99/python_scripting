# create function to check if the number is prime or not

def prime_check (n):
    for i in range (2,n // 2):
        if n % i == 0:
            return "Number is not prime"
    return "Number is prime"

n = int(input("N = "))
print(prime_check(n))