# create script to perform error handaling

try:
    x = 2 / 0
    print("X =",x)
except Exception as e:
    print("Error =",e)