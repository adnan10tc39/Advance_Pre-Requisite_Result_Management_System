from tkinter import  *
from course import CourseClass
from student import StudentClass
from result import resultClass
from report import reportClass
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
from tkinter import messagebox
import os
import sqlite3

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title('Pre-Requisite Result Management System')
        self.root.geometry('1350x700+0+0')

        #==========icons==========
        self.logo_dash = ImageTk.PhotoImage(file="Images/logo_p.png")
        #==========title==========
        title=Label(self.root,text='Pre-Requisite Result Management System',image=self.logo_dash,compound=LEFT,padx=10,font=("goudy old style",20,"bold"),
                    bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50 )

        #=========menu==========
        M_Frame = LabelFrame(self.root,text='Menus',font=("times new roman",15),bg='white')
        M_Frame.place(x=10,y=70,width=1340,height=80 )

        btn_course= Button(M_Frame, text="Course",font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',
                           cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40 )
        btn_student = Button(M_Frame, text="Student", font=('goudy old style', 15, 'bold'), bg='#0b5377', fg='white',
                            cursor="hand2",command=self.add_students).place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="Result", font=('goudy old style', 15, 'bold'), bg='#0b5377', fg='white',
                            cursor="hand2",command=self.add_result).place(x=460, y=5, width=200, height=40)
        btn_view = Button(M_Frame, text="View", font=('goudy old style', 15, 'bold'), bg='#0b5377', fg='white',
                            cursor="hand2",command=self.add_report).place(x=680, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text="Logout", font=('goudy old style', 15, 'bold'), bg='#0b5377', fg='white',
                            cursor="hand2",command=self.logout).place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="Exit", font=('goudy old style', 15, 'bold'), bg='#0b5377', fg='white',
                            cursor="hand2",command=self.exit_).place(x=1120, y=5, width=200, height=40)

        #==========contant window ========
        self.bg_image=Image.open('Images/bg.png')
        self.bg_image=self.bg_image.resize((920,350),Image.ANTIALIAS)
        self.bg_image=ImageTk.PhotoImage(self.bg_image)

        self.lbl_bg=Label(self.root,image=self.bg_image).place(x=400, y=180, width=920, height=350)

        #========== update details=======
        self.lbl_course = Label(self.root,text='Total Courses\n[ 0 ]', font=('goudy old style',20),bd=10,relief=RIDGE,bg='#e43b06',fg='white')
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text='Total Students\n[ 0 ]', font=('goudy old style', 20), bd=10,relief=RIDGE, bg='#0676ad', fg='white')
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text='Total Results\n[ 0 ]',font=('goudy old style', 20), bd=10,relief=RIDGE, bg='#038076', fg='white')
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        # ======= clock================
        self.lbl = Label(self.root, text='\nMycode Clock', font=('Book Antiqua', 25, 'bold'), compound=BOTTOM,fg='white', bg='#081923', bd=0)
        self.lbl.place(x=10, y=180, width=350, height=450)

        self.working()

        # ==========footer==========
        title = Label(self.root, text='PRMS-Pre-Requisite Result Management System\nContact Adnan Bajwa for any Technical Issue: 00923030395345',
                      font=("goudy old style", 12),bg='#262626',fg='white').pack(side=BOTTOM,fill=X)

        self.update_details()
    #==================== functions===================

    def update_details(self):

        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f'Total Courses\n[{len(cr)}]')

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f'Total Students\n[{len(cr)}]')

            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f'Total Results\n[{len(cr)}]')

            self.lbl_result.after(200, self.update_details)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

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

    def add_course(self):
        self.new_win =Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_students(self):
        self.new_win =Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)

    def add_result(self):
        self.new_win =Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    def add_report(self):
        self.new_win =Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno('confirm','Do you really want logout?',parent=self.root)
        if op==True:
            self.root.destroy()
            os.system('python login.py')

    def exit_(self):
        op=messagebox.askyesno('confirm','Do you really want Exit?',parent=self.root)
        if op==True:
            self.root.destroy()





if __name__ == '__main__':
    root =Tk()
    obj = RMS(root)
    root.mainloop()