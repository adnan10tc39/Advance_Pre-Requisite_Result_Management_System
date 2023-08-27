from tkinter import  *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
# import pymysql
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import os

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title('Login System')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='#021e2f')

        #==========background colors==============
        self.left_lbl = Label(self.root, bg='#08a3D2', bd=0)
        self.left_lbl.place(x=0, y=0, width=600, relheight=1)

        self.right_lbl = Label(self.root, bg='#031F3C', bd=0)
        self.right_lbl.place(x=600, y=0, relwidth=1, relheight=1)

        #================FRAMES================
        login_frame=Frame(self.root,bg='white')
        login_frame.place(x=250,y=100,width=800,height=500)

        login_title=Label(login_frame,text='LOGIN HERE',font=('times new roman',30,'bold'),bg='white',fg='#08A3D2').place(x=250,y=50)

        email_title = Label(login_frame, text='EMAIL ADDRESS', font=('times new roman',18, 'bold'), bg='white',fg='gray').place(x=250, y=150)
        self.txt_email = Entry(login_frame, font=('times new roman', 15),bg='lightgray')
        self.txt_email.place(x=250, y=180,width=350,height=35)

        pass_ = Label(login_frame, text='PASSWORD', font=('times new roman', 18, 'bold'), bg='white',fg='gray').place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=('times new roman', 15), bg='lightgray')
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, text='Register new Account?',font=('times new roman',14),bg='white',bd=0,fg='#B00857',cursor='hand2',
                         command=self.register_window).place(x=250,y=320)
        btn_forget = Button(login_frame, text='Forget Password?', font=('times new roman', 14), bg='white', bd=0,fg='red', cursor='hand2',
                            command=self.forget_password_window).place(x=450, y=320)
        btn_login = Button(login_frame, text='Login', font=('times new roman', 20,'bold'), fg='white',
                         bg='#B00857', cursor='hand2',command=self.login).place(x=250, y=380,width=180,height=40)


        #======= clock================
        self.lbl=Label(self.root,text='\nMycode Clock',font=('Book Antiqua',25,'bold'),compound=BOTTOM,fg='white',bg='#081923',bd=0)
        self.lbl.place(x=90,y=120,width=350,height=450)
        # self.clock_image()
        self.working()

    #==============functions================

    def clock_image(self,hr,min_,sec_):
        clock=Image.new('RGB',(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #for clock Image
        bg=Image.open('Images/c.png')
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))

        #Formula to rortate the clock anticlockwise
        #angle_in_radians = angle_in_degrees * math.pi/180
        #line_length=100
        #center_x=250
        #center_y=250
        #x2 or end_x=center_x - line_lenght * math.cos(angle_in_radians)
        # y2 or end_y=center_y - line_lenght * math.sin(angle_in_radians)

        #===for hour line====
        #(x1,y1,x2,y2)
        draw.line((200,200,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill='#DF005E',width=4)

        # ===for minuts line====
        # draw.line((200, 200, 280, 210), fill='blue', width=3)
        draw.line((200, 200, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill='white', width=3)
        # ===for second line====
        # draw.line((200, 200, 300, 240), fill='green', width=3)
        draw.line((200, 200, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill='yellow', width=2)

        draw.ellipse((195,195,210,210),fill='#1AD5D5')


        clock.save('Images/clock_new.png')

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        #make the angle of h,m,s
        hr= (h/12)*360
        min_=(m/60)*360
        sec_ = (s/ 60)*360
        self.clock_image(hr,min_,sec_)
        self.img = ImageTk.PhotoImage(file="Images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def register_window(self):
        self.root.destroy()
        import register

    def forget_password_window(self):
        if self.txt_email.get()=='':
            messagebox.showerror('Error','Please Enter the Email to reset the Password',parent=self.root)
        else:
            try:
                con=sqlite3.connect(database='rms.db')
                cur=con.cursor()
                cur.execute('select * from employee where email=?',(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Please Enter the Valid Email to reset the Password',parent=self.root)
                else:
                    con.close()
                    self.forget_pass_toplevel()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)

    def forget_pass_toplevel(self):
        self.root2=Toplevel()
        self.root2.title('Forget Password')
        self.root2.geometry('350x400+495+150')
        self.root2.config(bg='white')
        self.root2.focus_force()
        self.root2.grab_set()

        t=Label(self.root2,text='Forget Password',font=('times new roman',20,'bold'),bg='white',fg='red').place(x=0,y=10,relwidth=1)

        # -----------forget password-------
        qustion = Label(self.root2, text='Security Qustion', font=("times new roman", 15, "bold"), bg='white',
                        fg='gray').place(x=50, y=100)
        self.cmb_question = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_question['values'] = ('Select', 'Your First Pet Name', 'Your Birth Place', 'Your Best Friend Name')
        self.cmb_question.place(x=50, y=130, width=250)
        self.cmb_question.current(0)

        answer = Label(self.root2, text='Answer', font=("times new roman", 15, "bold"), bg='white', fg='gray').place(x=50,y=180)
        self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg='lightgray')
        self.txt_answer.place(x=50, y=210, width=250)

        newpassword = Label(self.root2, text='New Password', font=("times new roman", 15, "bold"), bg='white', fg='gray').place(x=50, y=260)
        self.txt_new_pass = Entry(self.root2, font=("times new roman", 15), bg='lightgray')
        self.txt_new_pass.place(x=50, y=290, width=250)

        btn_change_password=Button(self.root2,text='New Password',bg='green',fg='white',font=('times new roman',15,'bold'),command=self.forget_password).place(x=100,y=340)

    def forget_password(self):
        if self.cmb_question.get()=='Select' or self.txt_answer.get()=='' or self.txt_new_pass.get()=='':
            messagebox.showerror('Error','All fields are required',parent=self.root2)
        else:
            try:
                con=sqlite3.connect(database='rms.db')
                cur=con.cursor()
                cur.execute('select * from employee where email=? and question=? and answer=?',(self.txt_email.get(),self.cmb_question.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Please Select the correct Security question / Enter Answer',parent=self.root2)
                else:
                    cur.execute('update employee set password=? where email=?',(self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success','your password has been reset,please login with new password',parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)

    def reset(self):
        self.cmb_question.current(0)
        self.txt_answer.delete(0,END)
        self.txt_new_pass.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)

    def login(self):
        if self.txt_email.get()=='' or self.txt_pass_.get()=='':
            messagebox.showerror('Error','All fields are Required',parent=self.root)
        else:
            try:
                con=sqlite3.connect(database='rms.db')
                cur=con.cursor()
                cur.execute('select * from employee where email=? and password=?',(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Invalid Email and Password', parent=self.root)
                else:
                    messagebox.showinfo('Success', f'Welcome: {self.txt_email.get()}', parent=self.root)
                    self.root.destroy()
                    os.system('python dashboard.py')
                con.close()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)





root=Tk()
obj=login_window(root)
root.mainloop()