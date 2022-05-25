from cryptography.fernet import Fernet 

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: # wb: write in bytes mode
        key_file.write(key) '''

# write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")

key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f: #w: write, r: read, a: append
        for line in f.readlines():
            data = (line.rstrip()) # strip off the character line 
            user, passw = data.split("|") # this syntax, whenever sees this character splits it in different items
            # returns the string as the list, here, since only two things have been inputted, so only two elements would be split
            print("User:", user + ",", "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f: #w: write, r: read, a: append
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

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