employee_file = open("employees.txt", "r")
# r: read, w: write, a: append: add new info in the end of the file

print(employee_file.readable()) # this function helps to know if the files that we are trying to open are readable or not
# returns a boolean value

print(employee_file.read())

print(employee_file.readline()) # returns each line, line by line 

# print(employee_file.readlines()[1]) # reads all the lines and returns them as arrays

# Or we can do the following (works same as readlines()): -
for employee in employee_file.readlines():
    print(employee)

employee_file.close()