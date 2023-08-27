from tkinter import  *
from tkinter import ttk,messagebox
import sqlite3
class StudentClass:

    def __init__(self,root):
        self.root=root
        self.root.title('Pre-Requisite Result Management System')
        self.root.geometry('1200x480+100+200')
        self.root.config(bg='white')
        self.root.focus_force()

        # ==========title==========
        title = Label(self.root, text='Manage Student Details',font=("goudy old style", 20, "bold"),
                      bg="#033054", fg="white").place(x=10, y=15, width=1180, height=35)

        #=============Widgets========
        #===============column 1 statrt==========
        lbl_roll=Label(self.root,text='Roll No.',font=("goudy old style", 15, "bold"),bg='white').place(x=10, y=60)
        lbl_name = Label(self.root, text='Name', font=("goudy old style", 15, "bold"), bg='white').place(x=10, y=100)
        lbl_email = Label(self.root, text='Email', font=("goudy old style", 15, "bold"), bg='white').place(x=10, y=140)
        lbl_gender = Label(self.root, text='Gender', font=("goudy old style", 15, "bold"), bg='white').place(x=10, y=180)
        lbl_state = Label(self.root, text='State', font=("goudy old style", 15, "bold"), bg='white').place(x=10,y=220)
        lbl_address = Label(self.root, text='Address', font=("goudy old style", 15, "bold"), bg='white').place(x=10,y=260)

        #======entry fields======

        self.var_roll=StringVar()
        self.txt_roll = Entry(self.root,textvariable=self.var_roll, font=("goudy old style", 15, "bold"), bg='lightyellow')
        self.txt_roll.place(x=150, y=60,width=200)

        self.var_name = StringVar()
        txt_name = Entry(self.root,textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg='lightyellow').place(x=150, y=100,width=200)

        self.var_email = StringVar()
        txt_email = Entry(self.root,textvariable=self.var_email, font=("goudy old style", 15, "bold"), bg='lightyellow').place(x=150, y=140,width=200)

        self.var_gender = StringVar()
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender , values=('Select','Male','Female','Other'), font=("goudy old style", 15, "bold")
                                       ,state='readonly',justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)

        self.var_state = StringVar()
        self.txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, "bold"),bg='lightyellow')
        self.txt_state.place(x=150, y=220, width=150)

        lbl_city = Label(self.root, text='City', font=("goudy old style", 15, "bold"), bg='white').place(x=310, y=220)
        self.var_city = StringVar()
        self.txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, "bold"),bg='lightyellow')
        self.txt_city.place(x=380, y=220, width=100)

        lbl_pin = Label(self.root, text='Pin', font=("goudy old style", 15, "bold"), bg='white').place(x=500, y=220)
        self.var_pin = StringVar()
        self.txt_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15, "bold"),bg='lightyellow')
        self.txt_pin.place(x=560 , y=220, width=120)

        self.txt_address = Text(self.root, font=("goudy old style", 15, "bold"),bg ="lightyellow")
        self.txt_address.place(x=150, y=260,width=540,height=100)

        #==========column 1 ends==================

        #==============column 2 starts===============
        lbl_doc = Label(self.root, text='D.O.B', font=("goudy old style", 15, "bold"), bg='white').place(x=360, y=60)
        lbl_contact = Label(self.root, text='Contact', font=("goudy old style", 15, "bold"), bg='white').place(x=360, y=100)
        lbl_admission = Label(self.root, text='Admission', font=("goudy old style", 15, "bold"), bg='white').place(x=360, y=140)
        lbl_course = Label(self.root, text='Course', font=("goudy old style", 15, "bold"), bg='white').place(x=360, y=180)

        # ======entry fields======
        self.var_dob = StringVar()
        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"),bg='lightyellow')
        self.txt_dob.place(x=480, y=60, width=200)

        self.var_contact = StringVar()
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, "bold"),bg='lightyellow').place(x=480, y=100, width=200)

        self.var_admission = StringVar()
        txt_admission = Entry(self.root, textvariable=self.var_admission, font=("goudy old style", 15, "bold"),bg='lightyellow').place(x=480, y=140, width=200)

        self.course_list=['Select']
        #function call to update list
        self.fetch_course()
        self.var_course = StringVar()
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,values=self.course_list,font=("goudy old style", 15, "bold"),state='readonly', justify=CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.current(0)
        # ===========column 2 ends=========

        #===========Buttons=========
        self.btn_add=Button(self.root,text='Save',font=("goudy old style", 15, "bold"),bg ="#2196f3",fg='white',cursor='hand2',command=self.add)
        self.btn_add.place(x=150, y=400,width=110,height=40)

        self.btn_update = Button(self.root, text='Update', font=("goudy old style", 15, "bold"), bg="#4caf50", fg='white',cursor='hand2',command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="#f44336", fg='white',cursor='hand2',command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="#607d8b", fg='white',cursor='hand2',command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        #========= search panel========
        lbl_search_roll = Label(self.root, text='Roll No.',font=("goudy old style", 15, "bold"), bg='white').place(x=720, y=60)

        self.var_search = StringVar()
        self.search_roll = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"),bg='lightyellow')
        self.search_roll.place(x=870, y=60, width=180)

        btn_search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="#03a9f4", fg='white',
                            cursor='hand2',command=self.search).place(x=1070, y=60, width=120, height=28)

        #============ contant table======
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scroll_x = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.C_Frame, orient=VERTICAL)
        self.studentTable=ttk.Treeview(self.C_Frame,columns=('roll','name','email','gender','dob','contact',
                    'admission','course','state','city','pin','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.studentTable.xview)
        scroll_y.config(command=self.studentTable.yview)

        self.studentTable.heading('roll', text='Roll No')
        self.studentTable.column('roll', width=100)

        self.studentTable.heading('name', text='Name')
        self.studentTable.column('name', width=100)

        self.studentTable.heading('email', text='Email')
        self.studentTable.column('email', width=100)

        self.studentTable.heading('gender', text='Gender')
        self.studentTable.column('gender', width=100)

        self.studentTable.heading('dob', text='D.O.B')
        self.studentTable.column('dob', width=100)

        self.studentTable.heading('contact', text='Contact')
        self.studentTable.column('contact', width=100)

        self.studentTable.heading('admission', text='Admission')
        self.studentTable.column('admission', width=100)

        self.studentTable.heading('course', text='Course')
        self.studentTable.column('course', width=100)

        self.studentTable.heading('state', text='State')
        self.studentTable.column('state', width=100)

        self.studentTable.heading('city', text='City')
        self.studentTable.column('city', width=100)

        self.studentTable.heading('pin', text='Pin')
        self.studentTable.column('pin', width=100)

        self.studentTable.heading('address', text='Address')
        self.studentTable.column('address', width=200)

        self.studentTable.bind("<ButtonRelease-1>",self.get_data)
        self.studentTable['show']='headings'
        self.studentTable.pack(fill=BOTH,expand=1)
        self.show()

        #===================== functions ==========================

    def get_data(self,event):

        self.txt_roll.config(state='readonly')
        r =self.studentTable.focus()
        content = self.studentTable.item(r)
        row =content['values']
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_admission.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END,row[11])



    def add(self):

        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Roll Number Already Present", parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",
                                (
                                    self.var_roll.get(),
                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_contact.get(),
                                    self.var_admission.get(),
                                    self.var_course.get(),
                                    self.var_state.get(),
                                    self.var_city.get(),
                                    self.var_pin.get(),
                                    self.txt_address.get('1.0',END)
                                ))
                    con.commit()
                    messagebox.showinfo("Success","Studenet Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def show(self):

        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            self.studentTable.delete(*self.studentTable.get_children())
            for row in rows:
                self.studentTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def fetch_course(self):

        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):

        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Student from List", parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",
                                (
                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_contact.get(),
                                    self.var_admission.get(),
                                    self.var_course.get(),
                                    self.var_state.get(),
                                    self.var_city.get(),
                                    self.var_pin.get(),
                                    self.txt_address.get('1.0', END),
                                    self.var_roll.get()
                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Student updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):

        self.var_roll.set(''),
        self.var_name.set(''),
        self.var_email.set(''),
        self.var_gender.set('Select'),
        self.var_dob.set(''),
        self.var_contact.set(''),
        self.var_admission.set(''),
        self.var_course.set('Select'),
        self.var_state.set(''),
        self.var_city.set(''),
        self.var_pin.set(''),
        self.txt_address.delete('1.0', END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set('')


    def delete(self):

        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Student from List", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm",'Do you Really Want to Delete?',parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Student deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):

        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            cur.execute("select * from student where roll=?",(self.var_search.get(),))
            row = cur.fetchone()
            if row !=None:
                self.studentTable.delete(*self.studentTable.get_children())
                self.studentTable.insert('', END, values=row)
            else:
                messagebox.showerror('Error','No Record found',parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



if __name__ == '__main__':
    root =Tk()
    obj = StudentClass(root)
    root.mainloop()