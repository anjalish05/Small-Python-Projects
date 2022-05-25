master_pwd = input("What is the master password? ")

def view():
    pass

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f: #w: write, r: read, a: append
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones or quit? (view/add/q): ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add() 

    else:
        print("Invalid mode.")
        continue