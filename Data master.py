from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os
import os.path


def write_data():
    username_info = username.get()
    password_info = password.get()
    email_info = email.get()
    website_info = website.get()


    save_path = "94682167846512318"
    path_name = os.path.join(save_path, website_info + ".txt")
    with open(path_name, "w") as f:
        f.write("Website: " + website_info + "\n")
        f.write("Username: " + username_info + "\n")
        f.write("Password: " + password_info + "\n")
        f.write("Email: " + email_info + "\n")

    username_input.delete(0, END)
    password_input.delete(0, END)
    email_input.delete(0, END)
    website_input.delete(0, END)

    Label(nscreen, text="File created", fg="green", font=("calibri, 12")).pack()


def newf():

    global nscreen
    nscreen = Toplevel(screen)
    nscreen.title("New")
    nscreen.geometry("300x300")

    global username
    global password
    global email
    global website
    global username_input
    global password_input
    global email_input
    global website_input
    username = StringVar()
    password = StringVar()
    email = StringVar()
    website = StringVar()

    Label(nscreen, text="Enter your details below").pack()
    Label(nscreen, text="").pack()
    Label(nscreen, text="Username:").pack()
    username_input = Entry(nscreen, textvariable=username)
    username_input.pack()
    Label(nscreen, text="Password:").pack()
    password_input = Entry(nscreen, textvariable=password)
    password_input.pack()
    Label(nscreen, text="Email:").pack()
    email_input = Entry(nscreen, textvariable=email)
    email_input.pack()
    Label(nscreen, text="Website:").pack()
    website_input = Entry(nscreen, textvariable=website)
    website_input.pack()
    create_file = tk.Button(nscreen, text="Create File", width=10, height=1, command=write_data)
    create_file.pack()


def openf():

    oscreen = Toplevel(screen)
    oscreen.title("File Editor")
    oscreen.iconbitmap("C:")
    oscreen.geometry("500x450")

    def viewf():

        text_file = filedialog.askopenfilename(initialdir="94682167846512318",
                                                title="Open Text File", filetypes=(("Test File", "*.txt"),))
        text_file = open(text_file, "r")
        tf = text_file.read()

        my_text.insert(END, tf)
        text_file.close()

    def savef():
        text_file = filedialog.askopenfilename(initialdir="94682167846512318",
                                              title="Open Text File", filetypes=(("Test File", "*.txt"),))
        text_file = open(text_file, "w")
        tf = text_file.write(my_text.get(1.0, END))

        my_text.insert(END, tf)
        text_file.close()

    my_text = Text(oscreen, bg="white", width=40, height=15, font=("Helvetica", 16))
    my_text.pack(pady=20)

    open_button = tk.Button(oscreen, text="Open File", width=20, height=5, bg="#34495E", fg="white", command=viewf)
    open_button.pack(side=LEFT)

    save_button = tk.Button(oscreen, text="Save File", width=20, height=5, bg="#34495E", fg="white", command=savef)
    save_button.pack(side=LEFT)

    oscreen.mainloop()


def file_deleting():

    delete_text = dfile.get()

    directory = "94682167846512318"
    path_name = os.path.join(directory, delete_text + ".txt")
    os.remove(path_name)

    dfile_input.delete(0, END)

    Label(dscreen, text="File Deleted", fg="green", font=("calibri, 12")).pack()


def delf():

    global dscreen
    dscreen = Toplevel()
    dscreen.title("File Deleter")
    dscreen.geometry("300x150")

    global dfile
    global dfile_input
    dfile = StringVar()

    Label(dscreen, text="Enter below the name of the file you want to delete.").pack()
    Label(dscreen, text="").pack()
    Label(dscreen, text="File Name:").pack()
    dfile_input = Entry(dscreen, textvariable=dfile)
    dfile_input.pack()
    del_file = tk.Button(dscreen, text="Delete File", width=10, height=1, command=file_deleting)
    del_file.pack()


def main_screen():

    global screen
    screen = tk.Tk()
    screen.geometry("500x350")
    screen.title("Data master")
    screen.iconbitmap(r"data.ico")
    label = tk.Label(text="Welcome to Data master, please choose what you wish to do.",
          bg="#34495E", fg="white", width="700", height="3", font=("Calibri", 13))
    label.pack()

    Label(text="").pack()
    newFile = tk.Button(text="New File", width=15, height=2, bg="#34495E", fg="white", font=("Calibri", 13),
                        command=newf)
    newFile.pack()
    Label(text="").pack()
    viewFile = tk.Button(text="View File", width=15, height=2, bg="#34495E", fg="white", font=("Calibri", 13),
                         command=openf)
    viewFile.pack()
    Label(text="").pack()
    deleteFile = tk.Button(text="Delete File", width=15, height=2, bg="#34495E", fg="white", font=("Calibri", 13),
                         command=delf)
    deleteFile.pack()

    screen.mainloop()


main_screen()
