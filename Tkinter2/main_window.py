from tkinter import *


def log_in():
    login_page = Frame(root)
    login_page.place(relx=0.075, rely=0.1, relheight=0.8, relwidth=0.85)

    Label(login_page, text="Username: ").place(relx=0, rely=0.1, relwidth=0.3, relheight=0.1)
    Label(login_page, text="Password: ").place(relx=0, rely=0.3, relwidth=0.3, relheight=0.1)

    username_entry = Entry(login_page)
    username_entry.place(relx=0.4, rely=0.1, relwidth=0.5, relheight=0.1)

    pass_entry = Entry(login_page)
    pass_entry.place(relx=0.4, rely=0.3, relwidth=0.5, relheight=0.1)

    auth_btn = Button(login_page, text="Sign In", bd=1)
    auth_btn.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)


def sign_up():
    register_page = Frame(root, bg="blue")
    register_page.place(relx=0.075, rely=0.1, relheight=0.8, relwidth=0.85)


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

