from tkinter import  *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3

class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title('Pre-Requisite Result Management System')
        self.root.geometry('1200x480+100+200')
        self.root.config(bg='white')
        self.root.focus_force()

        # ==========title==========
        title = Label(self.root, text='Add Student Results', font=("goudy old style", 20, "bold"),
                      bg="orange", fg="#262626").place(x=10, y=15, width=1180, height=50)

        #==========widgets============
        lbl_select = Label(self.root, text='Select Student', font=("goudy old style", 20, "bold"), bg='white').place(x=50, y=100)
        lbl_name = Label(self.root, text='Name', font=("goudy old style", 20, "bold"), bg='white').place(x=50,y=160)
        lbl_course = Label(self.root, text='Course', font=("goudy old style", 20, "bold"), bg='white').place(x=50,y=220)
        lbl_marks_ob = Label(self.root, text='Marks Obtain', font=("goudy old style", 20, "bold"), bg='white').place(x=50, y=280)
        lbl_full_marks = Label(self.root, text='Full Marks', font=("goudy old style", 20, "bold"), bg='white').place(x=50, y=340)

        self.var_roll=StringVar()
        self.roll_no_list=["Select"]
        self.fetch_roll_no()
        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_no_list,
                                       font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.current(0)

        btn_search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="#03a9f4", fg='white',
                            cursor='hand2',command=self.search).place(x=500, y=100, width=100, height=28)
        #=======entries===================

        self.var_name = StringVar()
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"),bg='lightyellow',state='readonly')
        txt_name.place(x=280, y=160, width=320)

        self.var_course = StringVar()
        txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, "bold"),bg='lightyellow',state='readonly')
        txt_course.place(x=280, y=220, width=320)

        self.var_marks = StringVar()
        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 20, "bold"),bg='lightyellow')
        txt_marks.place(x=280, y=280, width=320)

        self.var_full_marks = StringVar()
        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 20, "bold"),bg='lightyellow')
        txt_full_marks.place(x=280, y=340, width=320)
        #==============buttons======
        btn_add = Button(self.root, text='Submit', font=("goudy old style", 15, "bold"), bg="lightgreen",
                         activebackground='lightgreen', cursor='hand2',command=self.add ).place(x=300, y=420, width=120, height=35)
        btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="lightgray",
                            cursor='hand2',activebackground='lightgray',command=self.clear).place(x=430, y=420, width=120, height=35)

        #===========image=================
        self.bg_image = Image.open('Images/result.jpg')
        self.bg_image = self.bg_image.resize((500, 300), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.lbl_bg = Label(self.root, image=self.bg_image).place(x=650, y=100)

    #============functions===============
    def fetch_roll_no(self):

        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_no_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):

        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            cur.execute("select name,course from student where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror('Error', 'No Record found', parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def add(self):

        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please first Search Student Record", parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?", (self.var_roll.get(),self.var_course.get()))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Result Already Present", parent=self.root)
                else:
                    percentage=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    cur.execute("insert into result(roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",
                                (
                                    self.var_roll.get(),
                                    self.var_name.get(),
                                    self.var_course.get(),
                                    self.var_marks.get(),
                                    self.var_full_marks.get(),
                                    "{:.1f}".format(percentage)

                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_roll.set('Select'),
        self.var_name.set(''),
        self.var_course.set(''),
        self.var_marks.set(''),
        self.var_full_marks.set('')

if __name__ == '__main__':
    root =Tk()
    obj = resultClass(root)
    root.mainloop()