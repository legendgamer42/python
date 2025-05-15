from cryptography.fernet import Fernet


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(":")
            print(f"User: {user}, Password: {fer.decrypt(passw.encode()).decode()}")
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt","a") as f:
        f.write(f"{name}:{fer.encrypt(pwd.encode()).decode()}\n")
while True:
    mode = input("Would you like to view or add the passwords(view/add) or q to quit: ")
    mode = mode.lower()

    if "add" in mode:
        add()
    elif "view" in mode:
        view()
    elif mode == "q":
        quit()
    else:
        print("Invalid mode!")
