dict1={"john":23,"bob":40,"rina":45} # dictionary contains students name with marks
name=input("Enter the student's name:") # Enter student's name
if name in dict1:
    print(f"{name} marks:{dict1[name]}")# prints marks of the student
else:
    print("The student not found") # name of student not found in the dict