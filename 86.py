# create script to use all function of tuple

import re

#   Print all values in tuple.
print("\n******************************************************************************\n")
my_tuple = ("ABC","BCD","CDE","DEF","EFG")
print("Tuple = ",my_tuple)

#   Append value in tuple.
print("\n******************************************************************************\n")
my_list=list(my_tuple)
my_list.append("FGH")
my_tuple=tuple(my_list)
print("Tuple = ",my_tuple)

#   Insert value at specific position.
print("\n******************************************************************************\n")
my_list=list(my_tuple)
my_list.insert(3,"XYZ")
my_tuple=tuple(my_list)
print("Tuple = ",my_tuple)

#   Count no of values/object in tuple.
print("\n******************************************************************************\n")
print("Total values/object in tuple = ",len(my_tuple))

#   Specific value/object is present in tuple or not.
print("\n******************************************************************************\n")
n = input("Enter the value = ")
if n in my_tuple:
    print(n,"is present in tuple.")
else:
    print(n,"is not present in tuple.")

#   Find position of specific value in tuple.
print("\n******************************************************************************\n")
n = input("Enter the value = ")
if n in my_tuple:
    print("Entered value position is = ",my_tuple.index(n))
else:
    print(n,"is not present in tuple.")

#   Print first three values of tuple.
print("\n******************************************************************************\n")
print("First three values = ",my_tuple[:3])

#   Print last three values of tuple
print("\n******************************************************************************\n")
print("Last three values = ",my_tuple[-3:])

#   Print 2 to 5 position values in tuple.
print("\n******************************************************************************\n")
print("Position 2 to 5 values = ",my_tuple[2:5])

#   Print 3rd position value in tuple.
print("\n******************************************************************************\n")
print("3rd position value = ",my_tuple[3])

#   Print 3rd position onwards all values in tuple.
print("\n******************************************************************************\n")
print("3rd position onwards all values = ",my_tuple[3:])

#   Print all values upto 3rd position.
print("\n******************************************************************************\n")
print("All values upto 3rd position = ",my_tuple[:3])

#   Find and replace perticular single value in tuple.
print("\n******************************************************************************\n")
n = input("Enter the value which you want to replace = ")
if n in my_tuple:
    my_list=list(my_tuple)
    x = input("Enter the new value = ")
    my_list[my_list.index(n)]=x
    my_tuple=tuple(my_list)
    print("New tuple = ",my_tuple)
else:
    print(n,"is not present in tuple.")

#   Find and replace perticular value in tuple (Multiple)
print("\n******************************************************************************\n")
n = input("Enter the value which you want to replace = ")
if n in my_tuple:
    my_list=list(my_tuple)
    x = input("Enter the new value = ")
    while n in my_list and n!=x:
        a = my_list.index(n)
        my_list[a]=x
    my_tuple=tuple(my_list)
    print("New tuple = ",my_tuple)
else:
    print(n,"is not present in tuple.")

#   Count the no of occurence of value in tuple.
print("\n******************************************************************************\n")
n = input("Enter the value which you want to count = ")
print("Counter of entered value is = ",my_tuple.count(n))

#   Print tuple in reverse order
print("\n******************************************************************************\n")
my_list=list(my_tuple)
my_list.reverse()
my_tuple=tuple(my_list)
print("Reverse tuple = ",my_tuple)

#   Extend tuple with another tuple.
print("\n******************************************************************************\n")
my_tuple2=("XYZ","WXY","VWX")
print("Extended tuple = ",my_tuple+my_tuple2)

#   Delete specific value from tuple.
print("\n******************************************************************************\n")
n = input("Enter the value which you want to remove = ")
if n in my_tuple:
    my_list=list(my_tuple)
    my_list.remove(n)
    my_tuple=tuple(my_list)
    print("Tuple = ",my_tuple)
else:
    print("Nothing to remove.")

#   Delete value from specific position.
print("\n******************************************************************************\n")
n = input("Enter the specific position in numbers which you want to remove = ")
x = re.findall("\D",n)
if not x:
    n=int(n)
    if n in range(0,len(my_tuple)):
        print("Hi")
        my_list=list(my_tuple)
        my_list.pop(n)
        my_tuple=tuple(my_list)
        print("Tuple = ",my_tuple)
else:
    print("Nothing to remove.")

#   Delete the last element from tuple
print("\n******************************************************************************\n")
my_list=list(my_tuple)
my_list.pop()
my_tuple=tuple(my_list)
print("Tuple = ",my_tuple)

#   Sort elements in tuple.
print("\n******************************************************************************\n")
my_list=list(my_tuple)
my_list.sort()
my_tuple=tuple(my_list)
print("Tuple = ",my_tuple)

#   Delete tuple.
print("\n******************************************************************************\n")
del(my_tuple)
print("The tuple is deleted.")
print("\n******************************************************************************\n")