employee_file = open("employees.txt", "a")

# employee_file = open("employees.txt", "w")
# write overwrites everything into whatever we'll write right now 

employee_file.write("\nToby - Human Resources")
# employee_file.write("\nKelly - Customer Service")


employee_file.close()

new_file = open("index.html", "w")

new_file.write("<p>This is HTML!</p>")