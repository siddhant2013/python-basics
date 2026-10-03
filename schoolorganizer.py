# step 1 - create a list of classmates
classmates = ["Aarav", "Priya", "Rahul", "Sneha", "Dev"]
print("Class list:", classmates)

# step 2 - access the list
print("Total students:", len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates [-1])
print("First three:", classmates[:3])

#step 3 - modifiy the list
classmates.append("Meera")
print("\nAfter adding Meera:", classmates)
classmates.remove("Dev")
print("After removing Dev:", classmates)
classmates.sort()
print("Sorted alphabetically:", classmates)
classmates.reverse()
print("Reversed:", classmates)

# step 4 - create a teacher dictionary
teacher = {"name": "Mr. Sharma", "subject": "Python", "experience": 5}
print("\nTeacher profile:", teacher)

# step 5 - dictionary operations
print("Subject:", teacher["subject"])
print("Experience", teacher.get("experience", "Not found"))
teacher["experience"] = 6
teacher["email"] = "sharma@school.com"
teacher.pop("experience")
print("Updated teacher profile:", teacher)

# step 6 - convert lists to a student directory
roll_numbers = [1,2,3,4,5]
names = ["Aarav", "Priya", "Rahul", "Sneha", "Meera"]
student_directory = dict(zip(roll_numbers, names))
print("\nStudent Directory:", student_directory)
print("Student at Roll 3:", student_directory [3])