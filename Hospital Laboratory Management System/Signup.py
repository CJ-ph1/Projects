import tkinter
import customtkinter
from tkinter import messagebox
from PIL import Image
import sqlite3

customtkinter.set_appearance_mode("light")
signup_window = customtkinter.CTk()
signup_window.title("WELCOME")
signup_window.geometry("990x660")


def clear():
    emailEntry.delete(0, tkinter.END)
    usernameEntry.delete(0, tkinter.END)
    passwordEntry.delete(0, tkinter.END)
    confirmEntry.delete(0, tkinter.END)
    check.set(0)


def connect_database():
    if emailEntry.get() == "" or usernameEntry.get() == "" or passwordEntry.get() == "" or confirmEntry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required")
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror("Error", "Password is not the same")
    elif check.get() == 0:
        messagebox.showerror("Error", "Please accept Terms & Conditions")
    else:
        try:
            con = sqlite3.connect("userdata.db")
            mycursor = con.cursor()
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS data(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    email TEXT, 
                    sername TEXT, 
                    password TEXT
                )
            """)

            # Check if username exists
            query = "select * from data where sername=?"
            mycursor.execute(query, (usernameEntry.get(),))
            row = mycursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Username Already Exists")
                return

            # Check if email exists
            query = "select * from data where email=?"
            mycursor.execute(query, (emailEntry.get(),))
            row = mycursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Email Already Exists")
                return

            # Insert new user
            query = "insert into data(email,sername,password) values(?,?,?)"
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration is successful")
            clear()
            signup_window.destroy()
            import Login
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {str(e)}")


def login_page():
    signup_window.destroy()
    import Login


Background_Image = customtkinter.CTkImage(Image.open("colors.jpg"), size=(990, 660))
Background_Image = customtkinter.CTkLabel(signup_window, image=Background_Image, text="")
Background_Image.place(x=0, y=0)

First_Frame = customtkinter.CTkFrame(master=signup_window, height=500, width=540, border_width=10)
First_Frame.place(x=50, y=70)

Background_Image = customtkinter.CTkImage(Image.open("Hospital2.jpg"), size=(535, 495))
Background_Image = customtkinter.CTkLabel(master=First_Frame, image=Background_Image, text="")
Background_Image.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

Second_Frame = customtkinter.CTkFrame(master=signup_window, height=500, width=350, border_width=2, fg_color="#eeeeee")
Second_Frame.place(relx=0.6, y=70)

user_login = customtkinter.CTkLabel(master=Second_Frame, text="CREATE AN ACCOUNT",
                                    font=('Century Gothic', 25)).place(relx=0.5, rely=0.12, anchor=tkinter.CENTER)

usernameLabels = customtkinter.CTkLabel(master=Second_Frame, text="Email").place(relx=0.21, rely=0.21,
                                                                                 anchor=tkinter.CENTER)
emailEntry = customtkinter.CTkEntry(Second_Frame, width=235, placeholder_text="Email")
emailEntry.place(relx=0.5, rely=0.26, anchor=tkinter.CENTER)

emailLabels = customtkinter.CTkLabel(master=Second_Frame, text="Username").place(relx=0.25, rely=0.32,
                                                                                 anchor=tkinter.CENTER)
usernameEntry = customtkinter.CTkEntry(master=Second_Frame, width=235, placeholder_text="Username")
usernameEntry.place(relx=0.5, rely=0.37, anchor=tkinter.CENTER)

passwordLabels = customtkinter.CTkLabel(master=Second_Frame, text="Password").place(relx=0.25, rely=0.43,
                                                                                    anchor=tkinter.CENTER)
passwordEntry = customtkinter.CTkEntry(master=Second_Frame, width=235, placeholder_text="Password")
passwordEntry.place(relx=0.5, rely=0.48, anchor=tkinter.CENTER)

confirmLabels = customtkinter.CTkLabel(master=Second_Frame, text="Confirm Password").place(relx=0.32, rely=0.54,
                                                                                           anchor=tkinter.CENTER)
confirmEntry = customtkinter.CTkEntry(master=Second_Frame, width=235, placeholder_text="Confirm Password")
confirmEntry.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

check = tkinter.IntVar()

terms_and_condition = tkinter.Checkbutton(Second_Frame, text="I agree to the Terms & Conditions", variable=check,
                                          font=("Open Sans", 10, "bold"))
terms_and_condition.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

signupButton = tkinter.Button(Second_Frame, width=15, text="Signup", activebackground="#eeeeee",
                              font=("Century Gothic", 11, "bold"), fg="black", cursor="hand2", command=connect_database)
signupButton.place(relx=0.5, rely=0.79, anchor=tkinter.CENTER)

loginLabel = tkinter.Label(Second_Frame, text="Already have an account?", bd=0, bg="#eeeeee", font=("Open Sans", 10))
loginLabel.place(relx=0.39, rely=0.89, anchor=tkinter.CENTER)

loginButton = tkinter.Button(Second_Frame, text="Login", font=("Open Sans", 10, "bold"), fg="black",
                             activebackground="#eeeeee",
                             cursor="hand2", command=login_page, bd=0, width=10)
loginButton.place(relx=0.75, rely=0.89, anchor=tkinter.CENTER)

signup_window.maxsize(990, 660)
signup_window.mainloop()