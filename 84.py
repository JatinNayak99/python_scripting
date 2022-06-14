# use lamda expression to find max number out of two numbers

max = lambda a ,b: "A" if a > b else "B"

a = int(input("A = "))
b = int(input("B = "))
print("MAX =",max(a,b))