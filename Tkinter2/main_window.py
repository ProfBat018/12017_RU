import string
from tkinter import *
from tkinter import messagebox
import pickle

users = dict()


def check_auth(username: str, password: str):
    chars = string.punctuation
    nums = string.digits
    alpha = string.ascii_letters

    elements = [chars, nums, alpha]

    user_check = False
    pass_check = False

    if len(username) >= 5 and username.isalnum():
        user_check = True

    if len(password) >= 8 and username not in password:
        count = 0
        for element in elements:
            for char in password:
                if char in element:
                    count += 1
                    break
        if count >= 2:
            pass_check = True

    if user_check and pass_check:
        return True
    return False


def check_user(username: str, password: str):

    file = open("data.txt", 'rb')

    users_from_file: dict = pickle.load(file)

    for key in users_from_file.keys():
        if username == key and users_from_file[key] == password:
            messagebox.showinfo("Success", "You logged in")

    file.close()


def log_in():


    # <editor-fold desc="Login Design">

    login_page = Frame(root)

    login_page.place(relx=0.075, rely=0.1, relheight=0.8, relwidth=0.85)

    Label(login_page, text="Username: ").place(relx=0, rely=0.1, relwidth=0.3, relheight=0.1)
    Label(login_page, text="Password: ").place(relx=0, rely=0.3, relwidth=0.3, relheight=0.1)

    username_entry = Entry(login_page)
    username_entry.place(relx=0.4, rely=0.1, relwidth=0.5, relheight=0.1)

    pass_entry = Entry(login_page)
    pass_entry.place(relx=0.4, rely=0.3, relwidth=0.5, relheight=0.1)

    auth_btn = Button(login_page, text="Sign In", bd=1, command=lambda:  check_user(username_entry.get(), pass_entry.get()))
    auth_btn.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)
    # </editor-fold>


def sign_up():
    def auth():
        auth_check_result = False

        if pass_entry.get() == confirm_pass_entry.get():
            auth_check_result = check_auth(username_entry.get(), pass_entry.get())
        else:
            messagebox.showerror("Passwords don't match", "Passwords must be same")

        if auth_check_result:
            file = open("data.bin", 'wb')

            users[username_entry.get()] = pass_entry.get()

            pickle.dump(users, file)
            file.close()

            messagebox.showinfo("Success", "You successfully registered")
        else:
            messagebox.showerror("Input Error", "Error, password must contain at least one digit or character")

    # <editor-fold desc="Register Design">

    register_page = Frame(root)
    register_page.place(relx=0.075, rely=0.1, relheight=0.8, relwidth=0.85)

    Label(register_page, text="Username: ", anchor=W).place(relx=0, rely=0.1, relwidth=0.3, relheight=0.1)
    Label(register_page, text="Password: ", anchor=W).place(relx=0, rely=0.3, relwidth=0.3, relheight=0.1)
    Label(register_page, text="Confirm: ", anchor=W).place(relx=0, rely=0.5, relwidth=0.4, relheight=0.1)

    username_entry = Entry(register_page)
    username_entry.place(relx=0.4, rely=0.1, relwidth=0.5, relheight=0.1)

    pass_entry = Entry(register_page)
    pass_entry.place(relx=0.4, rely=0.3, relwidth=0.5, relheight=0.1)

    confirm_pass_entry = Entry(register_page)
    confirm_pass_entry.place(relx=0.4, rely=0.5, relwidth=0.5, relheight=0.1)

    auth_btn = Button(register_page, text="Sign Up", bd=1, command=auth)
    auth_btn.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)

    # </editor-fold>


root = Tk()
root.title("Auth program")
root.resizable(False, False)
root.geometry("400x400")

root.option_add("*font", "Arial 14")

log_in_btn = Button(root, text="Login", bd=1, command=log_in)
log_in_btn.place(relx=0.3, rely=0, relwidth=0.2)

sign_up_btn = Button(root, text="Register", bd=1, command=sign_up)
sign_up_btn.place(relx=0.5, rely=0, relwidth=0.2)

root.mainloop()
