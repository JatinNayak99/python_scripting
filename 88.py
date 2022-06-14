# create script to use all function of dictionary

#   Print all values in Dictionary
print("\n******************************************************************************\n")
my_dict = {
    "Name"  : "Jatin",
    "Class" : "M.Sc.IT(IMS)",
    "Sem"   : "1"
    }
print("Dict. = ",my_dict)


#   Add Value in Dictionary
print("\n******************************************************************************\n")
my_dict["Enroll.No."] = "1002"
print("Dict. = ",my_dict)


#   Print Value using Key
print("\n******************************************************************************\n")
print("Name = ",my_dict["Name"])

#   Count no of values/object in Dictionary
print("\n******************************************************************************\n")
print("Number of value = ",len(my_dict))

#   Specific key/value is present in dictionary or not
print("\n******************************************************************************\n")
a = input("Enter the Key/Value = ")
if a in my_dict or a in my_dict.values():
    print("Entered values is present in dictionary.")
else:
    print("Entered values is not present in dictionary.")


#   Extend Dictionary with another Dictionary
print("\n******************************************************************************\n")
my_dict.update({"Mobile_No." : "9090909090"})
print("Dist. = ",my_dict)


#   Update value of specific Key in Dictionary
print("\n******************************************************************************\n")
my_dict["Name"]="Jay"
print("Dist. = ",my_dict)


#   Delete specific value from Dictionary 
print("\n******************************************************************************\n")
my_dict.pop("Mobile_No.")
print("Dist. = ",my_dict)

#   Delete Dictionary
print("\n******************************************************************************\n")
del (my_dict)
print("Dictionarys is deleted.")
print("\n******************************************************************************\n")