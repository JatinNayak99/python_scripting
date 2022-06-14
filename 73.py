# get string and count word

n = str(input("S = ")).lower()
a = 0
w = 0
for i in n:
    if i != " " and a == 0:
        w = w + 1
        a = 1
    elif i == " ":
        a = 0
print("Words =",w)

# print("Words =",len(n.split()))