from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import connection

root = Tk()
root.title("Python - Insert Data To Table")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

#==================================METHODS============================================


def insertData():
    if FIRSTNAME.get() == "" or LASTNAME.get() == "" or ADDRESS.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        connection.Database()
        connection.cursor.execute("INSERT INTO `member` (firstname, lastname, address, username, password) VALUES(?, ?, ?, ?, ?)", (str(
            FIRSTNAME.get()), str(LASTNAME.get()), str(ADDRESS.get()), str(USERNAME.get()), str(PASSWORD.get())))
        connection.conn.commit()
        FIRSTNAME.set("")
        LASTNAME.set("")
        ADDRESS.set("")
        USERNAME.set("")
        PASSWORD.set("")
        connection.cursor.close()
        connection.conn.close()
        txt_result.config(text="Inserted a data!", fg="green")

        displayData()


def displayData():
    tree.delete(*tree.get_children())
    connection.Database()
    connection.cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
    fetch = connection.cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(
            data[1], data[2], data[3], data[4], '****'))
    connection.cursor.close()
    connection.conn.close()


def Exit():
    result = tkMessageBox.askquestion(
        'Python - Insert Data To Table', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


#==================================VARIABLES==========================================
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
ADDRESS = StringVar()
USERNAME = StringVar()
PASSWORD = StringVar()

#==================================FRAME==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=600, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=300, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Right, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Right, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)

#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24),
                  text="Python - Insert Data To Table")
txt_title.pack()
txt_firstname = Label(Forms, text="Firstname:", font=('arial', 16), bd=15)
txt_firstname.grid(row=0, stick="e")
txt_lastname = Label(Forms, text="Lastname:", font=('arial', 16), bd=15)
txt_lastname.grid(row=1, stick="e")
txt_address = Label(Forms, text="Address:", font=('arial', 16), bd=15)
txt_address.grid(row=2, stick="e")
txt_username = Label(Forms, text="Username:", font=('arial', 16), bd=15)
txt_username.grid(row=3, stick="e")
txt_password = Label(Forms, text="Password:", font=('arial', 16), bd=15)
txt_password.grid(row=4, stick="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

#==================================ENTRY WIDGET=======================================
firstname = Entry(Forms, textvariable=FIRSTNAME, width=30)
firstname.grid(row=0, column=1)
lastname = Entry(Forms, textvariable=LASTNAME, width=30)
lastname.grid(row=1, column=1)
address = Entry(Forms, textvariable=ADDRESS, width=30)
address.grid(row=2, column=1)
username = Entry(Forms, textvariable=USERNAME, width=30)
username.grid(row=3, column=1)
password = Entry(Forms, textvariable=PASSWORD, show="*", width=30)
password.grid(row=4, column=1)

#==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Insert", command=insertData)
btn_create.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", command=Exit)
btn_exit.pack(side=LEFT)

#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Left, orient=VERTICAL)
scrollbarx = Scrollbar(Left, orient=HORIZONTAL)
tree = ttk.Treeview(Left, columns=("Firstname", "Lastname", "Address", "Username", "Password"),
                    selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Username', text="Username", anchor=W)
tree.heading('Password', text="Password", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=150)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.pack()

#==================================INITIALIZATION=====================================
displayData()

if __name__ == '__main__':
    root.mainloop()
