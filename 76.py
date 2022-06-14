# get string and find frequency of each character in a string

n = list(str(input("S = ")).lower())
for i in range (0,len(n)):
    if n[i] != "#":
        c = 1
        for j in range (i+1,len(n)):
            if n[i] == n[j]:
                c = c + 1
                n[j] = "#"
        print(n[i],"=",c)