import useful_tools
from Student import Student 

print(useful_tools.roll_dice(10))

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Dwight", "Business", 3.7, True)
# Object is just an instance of a class
# student1 and student2 are objects here

print(student1.name)

print(student1.on_honor_roll())

# self is the actual object 