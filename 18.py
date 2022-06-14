'''
input 5 subjet marks. count percentage and grade based on below condition:
condition           class
---------           -----
>=70%               distinction
60% to 69%          1st class
50% to 59%          2nd class
40% to 49%          3rd class
<40%                fail
'''

s1 = int(input("Subject 1 marks = "))
s2 = int(input("Subject 2 marks = "))
s3 = int(input("Subject 3 marks = "))
s4 = int(input("Subject 4 marks = "))
s5 = int(input("Subject 5 marks = "))

avg = (s1 + s2 + s3 + s4 + s5) / 5

if avg >= 70:
    print("Distinction")
elif avg >= 60:
    print("1st Class")
elif avg >= 50:
    print("2nd Class")
elif avg >= 40:
    print("3rd Class")
else:
    print("Fail")