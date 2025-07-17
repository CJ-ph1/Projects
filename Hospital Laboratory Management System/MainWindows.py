import customtkinter as ct
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import datetime

ct.set_appearance_mode("light")
global trv
counter = 0


def completelaboratory_page():
    global trv

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('', 'end', iid=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

    def search():
        q2 = q.get()
        try:
            con = sqlite3.connect("laboratory.db")
            cursor = con.cursor()
            query = "SELECT id, username, age, birthday, datetime, modeofpayment, price, specimen FROM data WHERE username LIKE ?"
            cursor.execute(query, ('%' + q2 + '%',))
            rows = cursor.fetchall()
            update(rows)
            con.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {str(e)}")

    def clear():
        try:
            con = sqlite3.connect("laboratory.db")
            cursor = con.cursor()
            query = "SELECT id, username, age, birthday, datetime, modeofpayment, price, specimen FROM data"
            cursor.execute(query)
            rows = cursor.fetchall()
            update(rows)
            con.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {str(e)}")

    def delete():
        selected = trv.selection()
        if not trv.selection():
            message = messagebox.showerror("Error", "Choose a data that you want to delete", parent=second)
        else:
            message = messagebox.askquestion("", "Are you sure you want to Delete?", parent=second)
            if message == "yes":
                try:
                    con = sqlite3.connect("laboratory.db")
                    cursor = con.cursor()
                    sql = "DELETE FROM data WHERE id = ?"
                    cursor.execute(sql, (selected[0],))
                    con.commit()
                    con.close()
                    trv.delete(selected[0])
                except sqlite3.Error as e:
                    messagebox.showerror("Error", f"Database error: {str(e)}")

    q = tkinter.StringVar()

    wrapper1 = tkinter.LabelFrame(second, text="Complete Laboratory", font=("Open Sans", 20))
    wrapper1.place(relx=0.5, rely=0.462, anchor=tkinter.CENTER)
    wrapper2 = tkinter.LabelFrame(second, text="Search Bar")
    wrapper2.place(relx=0.5, rely=0.044, anchor=tkinter.CENTER)

    lbl = tkinter.Label(wrapper2, text="Search", width=10)
    lbl.place(relx=0.05, rely=0.5, anchor=tkinter.CENTER)
    end = tkinter.Entry(wrapper2, textvariable=q, width=56)
    end.pack(side=tkinter.LEFT, padx=60)
    btn = tkinter.Button(wrapper2, text="Search", command=search, width=20)
    btn.pack(side=tkinter.LEFT, padx=10)
    cbtn = tkinter.Button(wrapper2, text="Clear", command=clear, width=20)
    cbtn.pack(side=tkinter.LEFT, padx=10)

    add_button = tkinter.Button(second, text="Add Information", font=("Open Sans", 13, "bold"), fg="black",
                                activebackground="#eeeeee", cursor="hand2", bd=0, width=80,
                                command=completelaboratory_data)
    add_button.place(relx=0.5, rely=0.866, anchor=tkinter.CENTER)

    delete_button = tkinter.Button(second, text="Delete", font=("Open Sans", 13, "bold"), fg="black",
                                   activebackground="#eeeeee", cursor="hand2", bd=0, width=80,
                                   command=delete)
    delete_button.place(relx=0.5, rely=0.92, anchor=tkinter.CENTER)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="#D3D3D3",
                    foreground="#000000",
                    rowheight=20,
                    fieldbackground="#D3D3D3"
                    )
    style.map('Treeview',
              background=[('selected', '#3A9ED6')])

    trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height=22)
    trv.pack()

    trv.column(1, width=100, minwidth=50, anchor=tkinter.CENTER)
    trv.column(2, width=50, minwidth=50, anchor=tkinter.CENTER)
    trv.column(3, width=150, minwidth=50, anchor=tkinter.CENTER)
    trv.column(4, width=200, minwidth=50, anchor=tkinter.CENTER)
    trv.column(5, width=100, minwidth=50, anchor=tkinter.CENTER)
    trv.column(6, width=100, minwidth=50, anchor=tkinter.CENTER)
    trv.column(7, width=100, minwidth=50, anchor=tkinter.CENTER)

    trv.heading(1, text="Name")
    trv.heading(2, text="Age")
    trv.heading(3, text="Birthday")
    trv.heading(4, text="Date")
    trv.heading(5, text="Payment")
    trv.heading(6, text="Price")
    trv.heading(7, text="Specimen")

    clear()  # Load initial data


def completelaboratory_data():
    global counter

    def clear():
        mainusernameEntry.delete(0, tkinter.END)
        mainageEntry.delete(0, tkinter.END)
        mainbirthdayEntry.delete(0, tkinter.END)
        priceEntry.delete(0, tkinter.END)
        specimenEntry.delete(0, tkinter.END)
        modeofpaymentEntry.set("Gcash")

    def reduce():
        global counter
        counter -= 2

    def refresh_data():
        completelaboratory_page()
        window.destroy()

    def another():
        completelaboratory_page()

    def insert_information():
        if mainusernameEntry.get() == "" or mainageEntry.get() == "" or mainbirthdayEntry.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=window)
        else:
            try:
                con = sqlite3.connect("laboratory.db")
                mycursor = con.cursor()
                mycursor.execute("""
                    CREATE TABLE IF NOT EXISTS data(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        age INTEGER,
                        birthday TEXT,
                        datetime TEXT,
                        modeofpayment TEXT,
                        price INTEGER,
                        specimen TEXT
                    )
                """)

                currentdatetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Check if username exists
                query = "select * from data where username=?"
                mycursor.execute(query, (mainusernameEntry.get(),))
                row = mycursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Username Already Exists", parent=window)
                    return

                # Insert new record
                query = """INSERT INTO data(username, age, birthday, datetime, modeofpayment, price, specimen) 
                           VALUES(?,?,?,?,?,?,?)"""
                mycursor.execute(query, (
                    mainusernameEntry.get(),
                    mainageEntry.get(),
                    mainbirthdayEntry.get(),
                    currentdatetime,
                    modeofpaymentEntry.get(),
                    priceEntry.get(),
                    specimenEntry.get()
                ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Information is stored", parent=window)
                clear()
                reduce()
                another()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Database error: {str(e)}", parent=window)

    if counter < 1:
        window = ct.CTkToplevel()
        window.geometry("890x560")
        window.title("Complete Laboratory")
        window_Image = ct.CTkImage(Image.open("colors1.jpg"), size=(890, 560))
        window_Image = ct.CTkLabel(master=window, image=window_Image, text="")
        window_Image.place(x=0, y=0)
        window_Frame1 = ct.CTkFrame(master=window, height=520, width=520, border_width=10)
        window_Frame1.place(x=25, y=20)
        window_Image1 = ct.CTkImage(Image.open("Hospital1.jpg"), size=(515, 515))
        window_Image1 = ct.CTkLabel(master=window_Frame1, image=window_Image1, text="")
        window_Image1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        window_Frame2 = ct.CTkFrame(master=window, height=520, width=315, border_width=2,
                                    fg_color="#eeeeee")
        window_Frame2.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

        user_window = ct.CTkLabel(master=window_Frame2, text="Complete Laboratory\n Information",
                                  font=('Century Gothic', 25))
        user_window.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        usernameLabels = ct.CTkLabel(master=window_Frame2, text="Name").place(relx=0.2, rely=0.2, anchor=tkinter.CENTER)
        mainusernameEntry = ct.CTkEntry(master=window_Frame2, width=235, placeholder_text="Name")
        mainusernameEntry.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

        ageLabels = ct.CTkLabel(master=window_Frame2, text="Age").place(relx=0.18, rely=0.31, anchor=tkinter.CENTER)
        mainageEntry = ct.CTkEntry(master=window_Frame2, width=235, placeholder_text="Age")
        mainageEntry.place(relx=0.5, rely=0.36, anchor=tkinter.CENTER)

        birthdayLabels = ct.CTkLabel(master=window_Frame2, text="Birthday").place(relx=0.22, rely=0.42,
                                                                                  anchor=tkinter.CENTER)
        mainbirthdayEntry = ct.CTkEntry(master=window_Frame2, width=235, placeholder_text="Birthday")
        mainbirthdayEntry.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)

        choices = ["Gcash", "Cash", "Debit Cards", "Credit Cards"]

        modeofpaymentLabels = ct.CTkLabel(master=window_Frame2, text="Mode Of Payment").place(relx=0.3, rely=0.53,
                                                                                              anchor=tkinter.CENTER)
        modeofpaymentEntry = ct.CTkComboBox(master=window_Frame2, width=235, values=choices)
        modeofpaymentEntry.set(choices[0])
        modeofpaymentEntry.place(relx=0.5, rely=0.58, anchor=tkinter.CENTER)

        priceLabels = ct.CTkLabel(master=window_Frame2, text="Price").place(relx=0.19, rely=0.64, anchor=tkinter.CENTER)
        priceEntry = ct.CTkEntry(master=window_Frame2, width=235, placeholder_text="Price")
        priceEntry.place(relx=0.5, rely=0.69, anchor=tkinter.CENTER)

        specimenLabels = ct.CTkLabel(master=window_Frame2, text="Specimen").place(relx=0.23, rely=0.75,
                                                                                  anchor=tkinter.CENTER)
        specimenEntry = ct.CTkEntry(master=window_Frame2, width=235, placeholder_text="Specimen")
        specimenEntry.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        insertButton = tkinter.Button(window_Frame2, width=12, text="Insert", activebackground="#eeeeee",
                                      font=("Century Gothic", 11, "bold"),
                                      fg="black", cursor="hand2", command=insert_information)
        insertButton.place(relx=0.3, rely=0.91, anchor=tkinter.CENTER)
        exitButton = tkinter.Button(window_Frame2, width=12, text="Exit", activebackground="#eeeeee",
                                    font=("Century Gothic", 11, "bold"),
                                    fg="black", cursor="hand2", command=refresh_data)
        exitButton.place(relx=0.7, rely=0.91, anchor=tkinter.CENTER)

        counter += 1

        window.resizable(False, False)
        window.mainloop()
    else:
        pass


def indicate(page):
    delete_pages()
    page()


def delete_pages():
    for frame in second.winfo_children():
        frame.destroy()


root = ct.CTk()
root.geometry("1170x700")
root.title("Hello")
bgcolor = ImageTk.PhotoImage(Image.open("Omsz.jpg"))
label = tkinter.Label(root, image=bgcolor).pack()

first = ct.CTkFrame(master=root, height=661, width=300, corner_radius=15, border_width=4, fg_color="#FFFFFF")
first.place(x=15, y=20)

frame1_title = ct.CTkLabel(master=first, text="HEALTH AVENUE \n LABORATORY", font=('Century Gothic', 30),
                           fg_color="#FFFFFF")
frame1_title.place(x=30, y=220)

frame1_name = ct.CTkLabel(master=first, text="SERVICES", font=('Century Gothic', 35), fg_color="#FFFFFF")
frame1_name.place(x=67, y=380)
frame1_name = ct.CTkLabel(master=first, text="---------------------------------------", fg_color="#FFFFFF")
frame1_name.place(x=64, y=420)

frame1_button = ct.CTkButton(master=first, text="Complete Laboratory", width=130, height=40,
                             fg_color="#40BD5A", hover=True, hover_color="#999999", font=("Century Gothic", 11, "bold"),
                             command=lambda: indicate(completelaboratory_page))
frame1_button.place(x=15, y=450)
frame2_button = ct.CTkButton(master=first, text="Eye Check Up", width=130, height=40,
                             font=("Century Gothic", 12, "bold"),
                             fg_color="#40BD5A", hover=True,
                             hover_color="#999999")  # command=lambda: indicate(eyecheckup_page)
frame2_button.place(x=155, y=450)
frame3_button = ct.CTkButton(master=first, text="Annual Physical Exam", font=("Arial", 11), width=130, height=40,
                             fg_color="#40BD5A", hover=True, hover_color="#999999")
frame3_button.place(x=15, y=500)
frame4_button = ct.CTkButton(master=first, text="Pre-Employment", width=130, height=40, fg_color="#40BD5A", hover=True,
                             hover_color="#999999", font=("Century Gothic", 11, "bold"))
frame4_button.place(x=155, y=500)
frame5_button = ct.CTkButton(master=first, text="Electrocardiogram", width=130, height=40, fg_color="#40BD5A",
                             hover=True, hover_color="#999999", font=("Century Gothic", 11, "bold"))
frame5_button.place(x=15, y=550)
frame6_button = ct.CTkButton(master=first, text="Medical Exam", width=130, height=40, fg_color="#40BD5A", hover=True,
                             hover_color="#999999", font=("Century Gothic", 11, "bold"))
frame6_button.place(x=155, y=550)

second = ct.CTkFrame(master=root, height=661, width=815, corner_radius=0, border_width=4, fg_color="#bcbcbc")
second.place(relx=0.63, rely=0.5, anchor=tkinter.CENTER)

bgcolor1 = ct.CTkImage(Image.open("Hospital2.jpg"), size=(807, 654))
bgcolor1 = ct.CTkLabel(second, image=bgcolor1, text="")
bgcolor1.place(rely=0.499, relx=0.499, anchor=tkinter.CENTER)

bgcolor2 = ct.CTkImage(Image.open("Logoimage.png"), size=(220, 220))
bgcolor2 = ct.CTkLabel(first, image=bgcolor2, text="")
bgcolor2.place(rely=0.18, relx=0.499, anchor=tkinter.CENTER)

root.resizable(False, False)
root.mainloop()