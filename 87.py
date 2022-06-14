# create script to use all function of set

#   Print all values in Set
print("\n******************************************************************************\n")
my_set = {"ABC","BCD","CDE"}
print("Set = ",my_set)


#   Add Value in Set
print("\n******************************************************************************\n")
my_set.add("XYZ")
print("Set = ",my_set)


#   Count no of values/object in Set
print("\n******************************************************************************\n")
print("Total value in set = ",len(my_set))


#   Specific value/object is present in Set or not
print("\n******************************************************************************\n")
a = input("Enter the value = ")
if a in my_set:
    print("Entered value is present in set.")
else:
    print("Entered value is not present in set.")


#   Extend Set with another Set
print("\n******************************************************************************\n")
my_set1 = {"PQR","VBX"}
my_set.update(my_set1)
print("Updated Set = ",my_set)

#   Find Difference between two Sets
print("\n******************************************************************************\n")
a = {"GHJ","JKL","ABC"}
z = a.difference(my_set)
print("Difference set = ",z)

#   Print Union of two Sets
print("\n******************************************************************************\n")
z = my_set.union(a)
print("Union set = ",z)

#   Print Intersection of Two Sets
print("\n******************************************************************************\n")
z = my_set.intersection(a)
print("Intersection set = ",z)

#   Check Weather Set is a subset of given Set
print("\n******************************************************************************\n")
b = {"ABC","CDE"}
z = b.issubset(my_set) 
print("Is Subset = ",z)


#   Check Weather Set is a superset of given Set
print("\n******************************************************************************\n")
z = my_set.issuperset(b) 
print("Is Superset = ",z)


#   Print Semmetric difference between two Sets
print("\n******************************************************************************\n")
z = my_set.symmetric_difference(b) 
print("Symmentric Difference = ",z)

#   Check Weather Two Sets are Disjoint or not
print("\n******************************************************************************\n")
z = my_set.isdisjoint(b) 
print("Is Disjoint = ",z)


#   Delete specific value from Set 
print("\n******************************************************************************\n")
my_set.discard("XYZ")
print("Set = ",my_set)

#   Delete Set
print("\n******************************************************************************\n")
del(my_set,a,b)
print("The Set is deleted.")
print("\n******************************************************************************\n")