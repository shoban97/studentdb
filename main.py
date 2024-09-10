from tkinter import *
from tkinter import ttk
import sqlite3

'''c=sqlite3.connect("Student.db")
curses=c.cursor()
curses.execute("CREATE TABLE IF NOT EXISTS Student(ID INTEGER, NAME VARCHAR(20), AGE INTEGER, DOB VARCHAR(20), GENDER VARCHAR(20), CITY VARCHAR(20)) ")
c.commit()
c.close()
print("Table Created")'''

class student:
    def __init__(self, main):
        self.main = main
        self.T_Frame = Frame(self.main, height=50, width=1200, background="yellow", bd=2, relief="groove")
        self.T_Frame.pack()
        self.Title = Label(self.T_Frame, text="Student Management System", font="arial 20 bold", width=1200, bg="yellow")
        self.Title.pack()

        self.Frame_1 = Frame(self.main, height=580, width=400, bd=2, relief="groove", bg="yellow")
        self.Frame_1.pack(side=LEFT)

        self.Frame_1.pack_propagate(0)

        Label(self.Frame_1, text="Student Details", background="yellow", font="arial 12 bold").place(x=20, y=20)

        self.id= Label(self.Frame_1, text="Id", background="yellow", font="arial 11 bold")
        self.id.place(x=40, y=60)
        self.id.Entry = Entry(self.Frame_1, width=40)
        self.id.Entry.place(x=150,y=60)

        self.name= Label(self.Frame_1, text="Name", background="yellow", font="arial 11 bold")
        self.name.place(x=40, y=100)
        self.name.Entry = Entry(self.Frame_1, width=40)
        self.name.Entry.place(x=150,y=100)

        self.age= Label(self.Frame_1, text="Age", background="yellow", font="arial 11 bold")
        self.age.place(x=40, y=140)
        self.age.Entry = Entry(self.Frame_1, width=40)
        self.age.Entry.place(x=150,y=140)

        self.dob= Label(self.Frame_1, text="DOB", background="yellow", font="arial 11 bold")
        self.dob.place(x=40, y=180)
        self.dob.Entry = Entry(self.Frame_1, width=40)
        self.dob.Entry.place(x=150,y=180)

        self.gender= Label(self.Frame_1, text="Gender", background="yellow", font="arial 11 bold")
        self.gender.place(x=40, y=220)
        self.gender.Entry = Entry(self.Frame_1, width=40)
        self.gender.Entry.place(x=150,y=220)
        
        self.city= Label(self.Frame_1, text="City", background="yellow", font="arial 11 bold")
        self.city.place(x=40, y=260)
        self.city.Entry = Entry(self.Frame_1, width=40)
        self.city.Entry.place(x=150,y=260)


        self.button_Frame = Frame(self.Frame_1, height=250, width=250, relief=GROOVE, bd=2, background="yellow")
        self.button_Frame.place(x=100,y=300)

        self.add=Button(self.button_Frame, text="Add", width=20, font="arial 11 bold", command=self.add)
        self.add.pack()
        self.delete=Button(self.button_Frame, text="Delete", width=20, font="arial 11 bold", command=self.delete)
        self.delete.pack()
        self.update=Button(self.button_Frame, text="Update", width=20, font="arial 11 bold", command=self.update)
        self.update.pack()
        self.clear=Button(self.button_Frame, text="Clear", width=20, font="arial 11 bold", command=self.clear)
        self.clear.pack()
                

        self.Frame_2 = Frame(self.main, height=580, width=800, bd = 2, relief="groove", bg="yellow")
        self.Frame_2.pack(side=RIGHT)

        self.tree = ttk.Treeview(self.Frame_2, columns=("c1","c2","c3","c4","c5","c6"), show='headings', height=25)
        
        self.tree.column("#1", anchor=CENTER, width=40)
        self.tree.heading("#1", text="Id")
        
        self.tree.column("#2", anchor=CENTER)
        self.tree.heading("#2", text="Name")
        
        self.tree.column("#3", anchor=CENTER, width=115)
        self.tree.heading("#3", text="DOB")

        self.tree.column("#4", anchor=CENTER, width=110)
        self.tree.heading("#4", text="Age")

        self.tree.column("#5", anchor=CENTER, width=110)
        self.tree.heading("#5", text="Gender")

        self.tree.column("#6", anchor=CENTER)
        self.tree.heading("#6", text="City")
        
        self.tree.insert("", index=0, values=(1, "vijay", 18, "13-12-2021", "male", "chennai"))

        self.tree.pack()

    def add(self):
        id=self.id.Entry.get()
        name=self.name.Entry.get()
        age=self.age.Entry.get()
        dob=self.dob.Entry.get()
        gender=self.gender.Entry.get()
        city=self.city.Entry.get()
        c=sqlite3.connect("Student.db")
        curses=c.cursor()
        curses.execute("INSERT INTO Student(ID, NAME, AGE, DOB, GENDER, CITY) VALUES(?,?,?,?,?,?)", (id, name, age, dob, gender, city))
        c.commit()
        c.close()
        print("Value Inserted")
        self.tree.insert("", index=0, values=(id, name, age, dob, gender, city))
        
    def delete(self):
        item=self.tree.selection()[0]
        selected_item=self.tree.item(item)['values'][0]
        print(selected_item)
        c=sqlite3.connect("Student.db")
        cursor=c.cursor()
        cursor.execute("DELETE FROM Student WHERE ID={}".format(selected_item))
        print("Value Deleted")
        c.commit()
        c.close()
        self.tree.delete(item)    
    def update(self):
        id=self.id.Entry.get()
        name=self.name.Entry.get()
        age=self.age.Entry.get()
        dob=self.dob.Entry.get()
        gender=self.gender.Entry.get()
        city=self.city.Entry.get()
        item=self.tree.selection()[0]
        selected_item=self.tree.item(item)['values'][0]
        c=sqlite3.connect("Student.db")
        cursor=c.cursor()
        cursor.execute("UPDATE Student SET ID=?, NAME=?, AGE=?, DOB=?, GENDER=?, CITY=? WHERE ID=?", (selected_item, name, age, dob, gender, city, selected_item))
        c.commit()
        c.close()
        print("Values Updated")
        self.tree.item(item, values=(id, name, age, dob, gender, city))        
    def clear(self):
        self.id.Entry.delete(0,END)
        self.name.Entry.delete(0,END)
        self.age.Entry.delete(0,END)
        self.dob.Entry.delete(0,END)
        self.gender.Entry.delete(0,END)
        self.city.Entry.delete(0,END)


main = Tk()
main.title("Student Management System")
main.resizable(False, False)
main.geometry("1200x600")

student(main)
main.mainloop()