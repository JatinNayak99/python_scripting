# create script to use all function of list

my_list = ["ABC","BCD","CDE","DEF","EFG"]

print("\n******************************************************************************")
print("Print all values in list.\n")
print("List = ",my_list)

print("\n******************************************************************************")
print("Append value in list.\n")
my_list.append("FGH")
print("List = ",my_list)

print("\n******************************************************************************")
print("Insert value at specific position.\n")
my_list.insert(3,"XYZ")
print("List = ",my_list)

print("\n******************************************************************************")
print("Count no of values in list.\n")
print("Total values in list = ",len(my_list))

print("\n******************************************************************************")
print("Check if the value is present in list or not.\n")
n = input("Value = ")
if n in my_list:
    print("Present")
else:
    print("Not Present")
    
print("\n******************************************************************************")
print("Find position of specific value in list.\n")
n = input("Value = ")
if n in my_list:
    print("Position =",my_list.index(n))
else:
    print("Value not Present")
    
print("\n******************************************************************************")
print("Print first three values of list.\n")
print("First three values = ",my_list[:3])

print("\n******************************************************************************")
print("Print last three values of list.\n")
print("Last three values = ",my_list[-3:])

print("\n******************************************************************************")
print("Print 2 to 5 position values in list.\n")
print("Position 2 to 5 values = ",my_list[2:5])

print("\n******************************************************************************")
print("Print 3rd position value in list.\n")
print("3rd position value = ",my_list[3])

print("\n******************************************************************************")
print("Print 3rd position onwards all values in list.\n")
print("3rd position onwards all values = ",my_list[3:])

print("\n******************************************************************************")
print("Print all values upto 3rd position.\n")
print("All values upto 3rd position = ",my_list[:3])

print("\n******************************************************************************")
print("Find and replace single value in list.\n")
n = input("Value to replace = ")
if n in my_list:
    x = input("New value = ")
    a = my_list.index(n)
    my_list[a]=x
    print("List = ",my_list)
else:
    print("Value not present")

print("\n******************************************************************************")
print("Find and replace multiple value in List (Multiple).\n")
n = input("Value to replace = ")
if n in my_list:
    x = input("New value = ")
    while n in my_list and n!=x:
        a = my_list.index(n)
        my_list[a]=x
    print("List = ",my_list)
else:
    print("Value not present")

print("\n******************************************************************************")
print("Count the no of occurence of value in list.\n")
n = input("Value to count = ")
print("Count =",my_list.count(n))

print("\n******************************************************************************")
print("Print list in reverse order.\n")
my_list.reverse()
print("Reverse list = ",my_list)

print("\n******************************************************************************")
print("Extend list with another list.\n")
my_list2=["XYZ","WXY","VWX"]
my_list.extend(my_list2)
print("Extended list = ",my_list)

print("\n******************************************************************************")
print("Delete specific value from list.\n")
n = input("Enter the value which you want to remove = ")
my_list.remove(n)
print("List = ",my_list)

print("\n******************************************************************************")
print("Delete value from specific position.\n")
n = input("Enter the specific position in numbers which you want to remove = ")
if n <= len(my_list):
    my_list.pop(n)
    print("List = ",my_list)
else:
    print("Nothing to remove.")

print("\n******************************************************************************")
print("Delete the last element from list.\n")
my_list.pop()
print("List = ",my_list)

print("\n******************************************************************************")
print("Sort elements in list.\n")
my_list.sort()
print("List = ",my_list)

print("\n******************************************************************************")
print("Delete list.\n")
del(my_list)
print("\nThe list is deleted.")
print("\n******************************************************************************")