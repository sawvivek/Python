
# List : list is a collection of items which are ordered and changeable. It allows duplicate members.It is defined by using square brackets []. It is a mutable data type, which means that you can change the content of a list after it has been created. Lists can contain items of different types, including other lists.
# t1 ="Vivek"
# t2 ="Ranjan"
# t3="Aditya"
# student=[t1,t2,t3]
# print(student)

# shopping=["Milk","Bread","Eggs","Butter"]
# print(shopping)
# # Adding items to a list:
# shopping.append("Cheese")
# print(shopping)

# # Removing items from a list:
# shopping.remove("Eggs")
# print(shopping)

# # Accessing items in a list:
# print(shopping[0])  # Output: Milk

# # Modifying items in a list:
# shopping[1] = "Whole Grain Bread"
# print(shopping)

# # List slicing:
# print(shopping[1:3])  # Output: ['Whole Grain Bread', 'Butter']

# # List length:
# print(len(shopping))  # Output: 4

# # List concatenation:
# more_shopping = ["Fruits", "Vegetables"]
# all_shopping = shopping + more_shopping
# print(all_shopping)

# # List repetition:
# repeated_shopping = shopping * 2
# print(repeated_shopping)

# # List membership:
# print("Milk" in shopping)  # Output: True
# print("Eggs" in shopping)  # Output: False


# # List methods:
# shopping.append("Yogurt")
# print(shopping)
# shopping.insert(2, "Juice")
# print(shopping)
# shopping.remove("Butter")
# print(shopping)
# shopping.pop(1)
# print(shopping)
# shopping.clear()
# print(shopping)

# operations on list
# age=[12,14,18,25,45,78,12,16,19,56,36,23,45,67,89,90]
# print(age.count(12)) # it will count the number of times 12 is present in the list

# print(len(age)) # it will give the length of the list
# print(age)

# age.sort() # it will sort the list in ascending order
# print(age)

# age.reverse() # it will reverse the order of the list
# print(age)

Student =['Vivek', 'Ranjan', 'Aditya']
print(Student)

Student.append('Rahul')
print(Student)

Student.sort()
print(Student)

print(Student[1:3]) # it will give the elements from index 1 to 2 (3-1)