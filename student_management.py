from tkinter import *
from tkinter import messagebox 
from tkinter import ttk


root = Tk()
root.geometry("800x450")
root.minsize(800, 450)
root.maxsize(800, 450)
root.title("NIT KKR- Student Management System")
root.configure(bg="#E6F0FA")

style = ttk.Style()
style.theme_use('default')
style.configure('TButton', font=('Helvetica', 11), padding=6)
style.configure('TLabel', font=('Helvetica', 11), background="#F0F4F8")
style.configure('TEntry', padding=5)

# Banner
banner = Frame(root, bg="#003366")
banner.pack(fill=X)
Label(banner, text="Welcome to NIT-KKR", fg="white", bg="#003366", font=("Helvetica", 26, "bold")).pack(pady=10)

# Frame for main buttons
f1 = Frame(root, bg="#D9E6F2", borderwidth=2, relief=RIDGE)
f1.pack(side=LEFT, anchor=NW, fill=Y)

# Main content frame
f2 = Frame(root, bg="#F0F4F8")
f2.pack(side=TOP, fill=BOTH, expand=True)

l2 = Label(f2, text="Student Management System", bg="#F0F4F8", fg="#003366", font=("Helvetica", 20, "bold"))
l2.place(relx=0.5, rely=0.4, anchor="center")

# For registering student
def submit():
    global namevalue, rollnovalue, branchvalue, phonevalue, addressvalue
    f = open("Student.txt", "r")
    str= f.read()
    if str.count(rollnovalue.get())==1:
        messagebox.showerror("Error", "Student already registered.")
    f.close()

    if namevalue.get() and rollnovalue.get() and branchvalue.get() and phonevalue.get() and addressvalue.get():
        if len(phonevalue.get()) == 10 and phonevalue.get().isdigit():
            if str.count(rollnovalue.get())==0:
                messagebox.showinfo("Success", "Student registered successfully")
                with open("Student.txt", "a") as f:
                    f.write(f"{namevalue.get()}, {rollnovalue.get()}, {branchvalue.get()}, {phonevalue.get()}, {addressvalue.get()}\n")
                namevalue.set("")
                rollnovalue.set("")
                branchvalue.set("")
                phonevalue.set("")
                addressvalue.set("")
        else:
            messagebox.showerror("Error", "Phone number should be 10 digits long and contain only digits")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

def register():
    global namevalue, rollnovalue, branchvalue, phonevalue, addressvalue
    root1 = Toplevel(root)
    root1.geometry("800x450")
    root1.minsize(800, 450)
    root1.maxsize(800, 450)
    root1.title("Register student")

    l3 = Label(root1, text="Register a Student", font="comicsansms 20 bold", background="#F0F4F8",fg="#003366", pady=30, padx=60).grid(row=0, column=3)

    name = Label(root1, text="Name")
    rollno = Label(root1, text="Roll Number")
    branch = Label(root1, text="Branch")
    phone = Label(root1, text="Phone Number")
    address = Label(root1, text="Address")

    name.grid(row=1, column=2, pady=10, padx=60)
    rollno.grid(row=2, column=2, pady=10, padx=60)
    branch.grid(row=3, column=2, pady=10, padx=60)
    phone.grid(row=4, column=2, pady=10, padx=60)
    address.grid(row=5, column=2, pady=10, padx=60)

    namevalue = StringVar()
    rollnovalue = StringVar()
    branchvalue = StringVar()
    phonevalue = StringVar()
    addressvalue = StringVar()

    nameentry = Entry(root1, textvariable=namevalue)
    rollnoentry = Entry(root1, textvariable=rollnovalue)
    branchentry = Entry(root1, textvariable=branchvalue)
    phoneentry = Entry(root1, textvariable=phonevalue)
    addressentry = Entry(root1, textvariable=addressvalue)


    nameentry.grid(row=1, column=3)
    rollnoentry.grid(row=2, column=3)
    branchentry.grid(row=3, column=3)
    phoneentry.grid(row=4, column=3)
    addressentry.grid(row=5, column=3)

    button5 = Button(root1, text='Register Student', width=20, pady=10, padx=10, command=submit)
    button5.grid(row=6, column=3, pady=20, padx=60)

# Viewing details
def details():
        root2.destroy()
        root3 = Toplevel(root)
        root3.geometry("800x450")
        root3.minsize(800, 450)
        root3.maxsize(800, 450)
        root3.title("View Details")
        found=0

        if rollnovalue.get():
            with open("Student.txt", "r") as f:
                for line in f:
                    l = line.split(", ")
                    if l[1] == rollnovalue.get():
                        found=1
                        l4 = Label(root3, text="Name :"+l[0], font="Calibri 20 ")
                        l4.pack(pady=10,padx=10,anchor=NW)
                        l5 = Label(root3, text="Roll number :"+l[1], font="Calibri 20 ")
                        l5.pack(pady=10,padx=10,anchor=NW)
                        l6 = Label(root3, text="Branch :"+l[2], font="Calibri 20 ")
                        l6.pack(pady=10,padx=10,anchor=NW)
                        l7 = Label(root3, text="Phone Number :"+l[3], font="Calibri 20 ")
                        l7.pack(pady=10,padx=10,anchor=NW)
                        l8 = Label(root3, text="Address :"+l[4], font="Calibri 20 ")
                        l8.pack(pady=10,padx=10,anchor=NW)
                        break
                if found==0:
                    messagebox.showerror("Error", "Student not found.")
        else:
            messagebox.showerror("Error", "Please,enter the roll number.")

def view():
    global rollnovalue,root2
    root2 = Toplevel(root)
    root2.geometry("800x450")
    root2.minsize(800, 450)
    root2.maxsize(800, 450)
    root2.title("View details")

    l4 = Label(root2, text="View details", font="comicsansms 20 bold", pady=30, padx=60).grid(row=0, column=3)

    roll = Label(root2, text="Enter Roll Number")
    roll.grid(row=1, column=2, pady=10, padx=60)
    rollnovalue = StringVar()
    rollentry = Entry(root2, textvariable=rollnovalue)
    rollentry.grid(row=1, column=3)

    button6 = Button(root2, text='View Details', width=20, pady=10, padx=10, command=details)
    button6.grid(row=2, column=3, pady=20, padx=60)

# Academics
def submit1():
    global namevalue, rollnovalue, sgpavalue, cgpavalue
    if namevalue.get() and rollnovalue.get() and sgpavalue.get() and cgpavalue.get():
        if int(sgpavalue.get())<=10 and int(cgpavalue.get())<=10:
            messagebox.showinfo("Success","Student's Academics registered successfully.")
            root4.destroy()
            with open("Academic.txt", "a") as f:
                f.write(f"{namevalue.get()}, {rollnovalue.get()}, {sgpavalue.get()}, {cgpavalue.get()}\n")
            namevalue.set("")
            rollnovalue.set("")
            sgpavalue.set("")
            cgpavalue.set("")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

def acad():
    global rollnovalue, root4, namevalue, sgpavalue, cgpavalue

    roll_number = rollnovalue.get() 
    found = False

    with open("Academic.txt", "r") as f:
        for line in f:
            l = line.split(", ")
            if l[1] == roll_number:
                found = True
                root4 = Toplevel(root)
                root4.geometry("800x450")
                root4.minsize(800, 450)
                root4.maxsize(800, 450)
                root4.title("Academic Details")

                l4 = Label(root4, text="Name: " + l[0], font="Calibri 20 ")
                l4.pack(pady=10, padx=10, anchor=NW)
                l5 = Label(root4, text="Roll number: " + l[1], font="Calibri 20 ")
                l5.pack(pady=10, padx=10, anchor=NW)
                l6 = Label(root4, text="SGPA: " + l[2], font="Calibri 20 ")
                l6.pack(pady=10, padx=10, anchor=NW)
                l7 = Label(root4, text="CGPA: " + l[3], font="Calibri 20 ")
                l7.pack(pady=10, padx=10, anchor=NW)
                break

    if not found:
        messagebox.showerror("Error","Please register student's academics.")
        root4 = Toplevel(root)
        root4.geometry("800x450")
        root4.minsize(800, 450)
        root4.maxsize(800, 450)
        root4.title("Register Academic Information")

        l6 = Label(root4, text="Register Academic Information", font="comicsansms 20 bold", pady=30, padx=60)
        l6.grid(row=0,column=3)

        name = Label(root4, text="Name")
        name.grid(row=1, column=2, pady=10, padx=60)
        rollno = Label(root4, text="Roll Number")
        rollno.grid(row=2, column=2, pady=10, padx=60)
        sgpa = Label(root4, text="SGPA")
        sgpa.grid(row=3, column=2, pady=10, padx=60)
        cgpa = Label(root4, text="CGPA")
        cgpa.grid(row=4, column=2, pady=10, padx=60)

        namevalue = StringVar()
        rollnovalue = StringVar()
        sgpavalue = StringVar()
        cgpavalue = StringVar()

        nameentry = Entry(root4, textvariable=namevalue)
        nameentry.grid(row=1, column=3)
        rollnoentry = Entry(root4, textvariable=rollnovalue)
        rollnoentry.grid(row=2, column=3)
        sgpaentry = Entry(root4, textvariable=sgpavalue)
        sgpaentry.grid(row=3, column=3)
        cgpaentry = Entry(root4, textvariable=cgpavalue)
        cgpaentry.grid(row=4, column=3)

        button5 = Button(root4, text='Submit', width=20, pady=10, padx=10, command=submit1)
        button5.grid(row=5, column=3, pady=20, padx=60)


def Academics():
    global namevalue, rollnovalue,root4

    root4 = Toplevel(root)
    root4.geometry("800x450")
    root4.minsize(800, 450)
    root4.maxsize(800, 450)
    root4.title("Academics")

    l5 = Label(root4, text="Academic Information", font="comicsansms 20 bold", pady=30, padx=60)
    l5.grid(row=0, column=3)

    roll = Label(root4, text="Enter Roll Number")
    roll.grid(row=1, column=2, pady=10, padx=60)
    rollnovalue = StringVar()
    rollentry = Entry(root4, textvariable=rollnovalue)
    rollentry.grid(row=1, column=3)

    button7 = Button(root4, text='View Academic Details', width=20, pady=10, padx=10, command=acad)
    button7.grid(row=2, column=3, pady=20, padx=60)

# Fee Status
def paid():
    class FeePayment:
        def __init__(self,rollnum,amt):
            self.rollnum=rollnum
            self.amt=amt
            f2=open("fee.txt","a")
            f2.write(f" {self.rollnum}, {self.amt},true\n")
            f2.close()
        def showReceipt(self):
            r3 = Toplevel(root)
            r3.geometry("800x450")
            r3.minsize(800, 450)
            r3.maxsize(800, 450)
            r3.title("Fee Receipt")
            lab4 = Label(r3, text="Fee Receipt", font="Calibri 14 ")
            lab4.pack(pady=10,padx=10,anchor=NW)
            lab5 = Label(r3, text="Roll number :"+self.rollnum, font="Calibri 14 ")
            lab5.pack(pady=10,padx=10,anchor=NW)
            lab6 = Label(r3, text="Fee paid :"+self.amt, font="Calibri 14 ")
            lab6.pack(pady=10,padx=10,anchor=NW)
    if int(amountvalue.get())==payablefee:
        f1=FeePayment(rollnovalue.get(),amountvalue.get())
        f1.showReceipt()
    else:
        messagebox.showerror("Error","Enter correct amount.")
def proceed():
    global amountvalue
    r1.destroy()
    r2 = Toplevel(root)
    r2.geometry("800x450")
    r2.minsize(800, 450)
    r2.maxsize(800, 450)
    r2.title("Fee Payment")

    lab3 = Label(r2, text="Fee Payment", font="Algerain 20 bold", pady=30, padx=60).grid(row=0, column=3)

    roll = Label(r2, text="Enter Roll Number")
    roll.grid(row=1, column=2, pady=10, padx=60)
    rollnovalue = StringVar()
    rollentry = Entry(r2, textvariable=rollnovalue)
    rollentry.grid(row=1, column=3)

    amount = Label(r2, text="Amount to be paid")
    amount.grid(row=2, column=2, pady=10, padx=60)
    amountvalue = StringVar()
    amountentry = Entry(r2, textvariable=amountvalue)
    amountentry.grid(row=2, column=3)

    b4 = Button(r2, text='Pay and Show Receipt', width=30, pady=10, padx=10,command=paid)
    b4.grid(row=3, column=3, pady=20, padx=60)

def status():
    f4 = open("fee.txt", "r")
    str2= f4.read()
    f4.close()
    if str2.count(rollnovalue.get())==1:
        messagebox.showerror("Error", "Your fee is already paid.")
    else:
        with open ("student.txt","r") as f:
            found=False
            for line in f:
                l = line.split(", ")
                if l[1] == rollnovalue.get():
                    found = True
        if found==True:
            b1.destroy()
            cateogory = Label(r1, text="Enter your Cateogory")
            cateogory.grid(row=2, column=2, pady=10, padx=60)
            cateogoryvalue = StringVar()
            cateogoryentry = Entry(r1, textvariable=cateogoryvalue)
            cateogoryentry.grid(row=2, column=3)
            def calculate_fee():
                global payablefee
                payablefee = 0
                category = cateogoryvalue.get()
                if category == "General":
                    payablefee = 20000
                elif category == "OBC" or category == "GEN-EWS":
                    payablefee = 10000
                elif category == "SC" or category == "ST":
                    payablefee = 5000

                lab2 = Label(r1, text="Fee to be paid is: " + str(payablefee), font="Calibri 14 bold", pady=30, padx=60)
                lab2.grid(row=3, column=3)
                b2.destroy()
                b3 = Button(r1, text='Proceed to pay fee', width=30, pady=10, padx=10, command=proceed)
                b3.grid(row=4, column=3, pady=20, padx=60)

            b2 = Button(r1, text='Show fee to be paid', width=30, pady=10, padx=10, command=calculate_fee)
            b2.grid(row=4, column=3, pady=20, padx=60)
        else:
            messagebox.showerror("Error","Student not found.First register the student.")
            r1.destroy()
def fee():
    global rollnovalue,r1,b1
    r1 = Toplevel(root)
    r1.geometry("800x450")
    r1.minsize(800, 450)
    r1.maxsize(800, 450)
    r1.title("Fee Status")

    lab1 = Label(r1, text="Fee Status", font="Algerain 20 bold", pady=30, padx=60).grid(row=0, column=3)

    roll = Label(r1, text="Enter Roll Number")
    roll.grid(row=1, column=2, pady=10, padx=60)
    rollnovalue = StringVar()
    rollentry = Entry(r1, textvariable=rollnovalue)
    rollentry.grid(row=1, column=3)

    b1 = Button(r1, text='View Fee Status', width=30, pady=10, padx=10,command=status)
    b1.grid(row=2, column=3, pady=20, padx=60)


# Basic layout of our student management system
f1 = Frame(root, bg="grey", borderwidth=10, relief=RIDGE)
f1.pack(side=LEFT, anchor=NW, fill=Y)

button1 = Button(f1, text='Register Student', width=20, borderwidth=4, pady=20, padx=20, relief=SUNKEN, command=register)
button1.pack(pady=15)

button2 = Button(f1, text='View Student', width=20, borderwidth=4, pady=20, padx=20, relief=SUNKEN, command=view)
button2.pack(pady=15)

button3 = Button(f1, text='Fee status', width=20, borderwidth=4, pady=20, padx=20, relief=SUNKEN,command=fee)
button3.pack(pady=15)

button4 = Button(f1, text='Academic Info', width=20, borderwidth=4, pady=20, padx=20, relief=SUNKEN,command=Academics)
button4.pack(pady=15)

f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill=BOTH, expand=True)

l1 = Label(f2, text="Welcome to NIT-KKR", bg="grey", fg="#FF0000", borderwidth=4, relief=SUNKEN, font=("Algerain", 30, "bold"))
l1.pack(pady=130)

l2 = Label(f2, text="Student Management System", bg="grey", fg="#00FF00", borderwidth=4, relief=SUNKEN, font=("Algerain", 25, "bold"))
l2.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()