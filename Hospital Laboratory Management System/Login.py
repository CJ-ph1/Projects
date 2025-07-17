import tkinter
import customtkinter
from tkinter import messagebox
from PIL import Image
import sqlite3
global counter
counter = 1

def forget_pass():
    global counter
    def change_password():
        if newusernameEntry.get() == "" or newpasswordEntry.get() == "" or confirmnewEntry.get() == "":
            messagebox.showerror("Error","All Fields Are Required",parent=window)
        elif newpasswordEntry.get() != confirmnewEntry.get():
            messagebox.showerror("Error","Password is not matched",parent=window)
        else:
            try:
                con = sqlite3.connect("userdata.db")
                mycursor = con.cursor()
                query = "select * from data where sername=?"
                mycursor.execute(query,(newusernameEntry.get(),))
                row = mycursor.fetchone()
                if row is None:
                    messagebox.showerror("Error","Wrong Username",parent=window)
                else:
                    query = "update data set password=? where sername=?"
                    mycursor.execute(query,(newpasswordEntry.get(),newusernameEntry.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password is reset",parent=window)
                    window.destroy()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Database error: {str(e)}", parent=window)

    if counter < 2:
        window = customtkinter.CTkToplevel()
        window.geometry("790x460")
        window.title("Change Password")
        window_Image = customtkinter.CTkImage(Image.open("colors1.jpg"), size=(790, 460))
        window_Image = customtkinter.CTkLabel(master=window, image=window_Image, text="")
        window_Image.place(x=0, y=0)
        window_Frame1 = customtkinter.CTkFrame(master=window, height=420, width=420, border_width=10)
        window_Frame1.place(x=25, y=20)
        window_Image1 = customtkinter.CTkImage(Image.open("Hospital2.jpg"), size=(415, 415))
        window_Image1 = customtkinter.CTkLabel(master=window_Frame1, image=window_Image1, text="")
        window_Image1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        window_Frame2 = customtkinter.CTkFrame(master=window, height=420, width=315, border_width=2,
                                              fg_color="#eeeeee")
        window_Frame2.place(relx=0.77, rely=0.5, anchor=tkinter.CENTER)
        user_window = customtkinter.CTkLabel(master=window_Frame2, text="RESET PASSWORD",
                                            font=('Century Gothic', 25))
        user_window.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        usernameLabels = customtkinter.CTkLabel(master=window_Frame2, text="Username").place(relx=0.23, rely=0.25, anchor=tkinter.CENTER)
        newusernameEntry = customtkinter.CTkEntry(master=window_Frame2, width=235, placeholder_text="Username")
        newusernameEntry.place(relx=0.5, rely=0.32, anchor=tkinter.CENTER)

        passwordLabels = customtkinter.CTkLabel(master=window_Frame2, text="Password").place(relx=0.23, rely=0.39, anchor=tkinter.CENTER)
        newpasswordEntry = customtkinter.CTkEntry(master=window_Frame2, width=235, placeholder_text="Password")
        newpasswordEntry.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

        confirmLabels = customtkinter.CTkLabel(master=window_Frame2, text="Confirm Password").place(relx=0.3, rely=0.52, anchor=tkinter.CENTER)
        confirmnewEntry = customtkinter.CTkEntry(master=window_Frame2, width=235, placeholder_text="Confirm Password")
        confirmnewEntry.place(relx=0.5, rely=0.58, anchor=tkinter.CENTER)

        resetButton = tkinter.Button(window_Frame2, width=15, text="Reset", activebackground="#eeeeee",
                                     font=("Century Gothic", 13, "bold"),
                                     fg="black", cursor="hand2", command=change_password)
        resetButton.place(relx=0.5, rely=0.74, anchor=tkinter.CENTER)
        counter += 1
    else:
        pass
    window.maxsize(790,460)
    window.mainloop()

def login_user():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        tkinter.messagebox.showerror("Error","All Fields Are Required")
    else:
        try:
            con = sqlite3.connect("userdata.db")
            mycursor = con.cursor()
            query = "select * from data where sername=? and password=?"
            mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                login_window.destroy()
                import MainWindows
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {str(e)}")

def signup_page():
    login_window.destroy()
    import Signup

customtkinter.set_appearance_mode("light")

login_window = customtkinter.CTk()
login_window.title("WELCOME")
login_window.geometry("990x660")

def user_enter(event):
    if usernameEntry.get()=="Username":
        usernameEntry.delete(0,tkinter.END)

def password_enter(event):
    if passwordEntry.get()=="Password":
        passwordEntry.delete(0,tkinter.END)

Background_Image = customtkinter.CTkImage(Image.open("colors.jpg"), size=(990,660))
Background_Image = customtkinter.CTkLabel(login_window, image=Background_Image, text="")
Background_Image.place(x=0,y=0)

First_Frame = customtkinter.CTkFrame(master=login_window, height=500, width=540, border_width=10)
First_Frame.place(x=50, y=70)

Background_Image = customtkinter.CTkImage(Image.open("Hospital2.jpg"), size=(535,495))
Background_Image = customtkinter.CTkLabel(master=First_Frame, image=Background_Image, text="")
Background_Image.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


Second_Frame = customtkinter.CTkFrame(master=login_window, height=500, width=350, border_width=2, fg_color="#eeeeee")
Second_Frame.place(relx=0.6, y=70)

user_login = customtkinter.CTkLabel(master=Second_Frame, text="USER LOGIN",
                                    font=('Century Gothic', 35)).place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

usernameEntry = customtkinter.CTkEntry(master=Second_Frame, width=235, placeholder_text="Username")
usernameEntry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
passwordEntry = customtkinter.CTkEntry(master=Second_Frame, width=235, placeholder_text="Password", show="*")
passwordEntry.place(relx=0.5, rely=0.37, anchor=tkinter.CENTER)

forgotButton = tkinter.Button(Second_Frame, text="Forgot Password?", bd=0, bg="#eeeeee",
                              activebackground="#eeeeee", cursor="hand2", command=forget_pass)
forgotButton.place(relx=0.55, rely=0.41)

loginButton = tkinter.Button(Second_Frame, width=15, text="Login", activebackground="#eeeeee", font=("Century Gothic", 11, "bold"),
                             fg="black", cursor="hand2", command=login_user)
loginButton.place(relx=0.5, rely=0.54, anchor=tkinter.CENTER)

randomtext = tkinter.Label(Second_Frame, text="---------------------------------------------", bg="#eeeeee")
randomtext.place(relx=0.5, rely=0.62, anchor=tkinter.CENTER)

logo1_picture = customtkinter.CTkImage(Image.open("logoo1.png"), size=(60,60))
logo1 = customtkinter.CTkLabel(master=Second_Frame, image=logo1_picture, text="")
logo1.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

logo2_picture = customtkinter.CTkImage(Image.open("logoo3.png"), size=(60,60))
logo2 = customtkinter.CTkLabel(master=Second_Frame, image=logo2_picture, text="")
logo2.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

logo3_picture = customtkinter.CTkImage(Image.open("logoo2.png"), size=(60,60))
logo3 = customtkinter.CTkLabel(master=Second_Frame, image=logo3_picture, text="")
logo3.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)


signupLabel = tkinter.Label(Second_Frame, text="Dont have an account?", bd=0, bg="#eeeeee", font=("Open Sans", 10))
signupLabel.place(relx=0.5, rely=0.83, anchor=tkinter.CENTER)

newaccountButton = tkinter.Button(Second_Frame, text="Create new one", font=("Open Sans", 10, "bold"), fg="black", activebackground="#eeeeee",
                                  cursor="hand2", command=signup_page, bd=0, width=19)
newaccountButton.place(relx=0.5, rely=0.89, anchor=tkinter.CENTER)

login_window.maxsize(990,660)
login_window.mainloop()