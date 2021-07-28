import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image

class Profile:
    userD=''
    def __init__(self,root,dline):
        Profile.userD=dline
        userdata=dline.split('|')

        self.root=root
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=1)
        self.my_canvas = Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.topnav=Frame(self.my_canvas)
        self.topnav.pack(side=TOP,fill=X)
        homeB = Button(self.topnav, text="Home",height=3,borderwidth=4, relief="groove",bg="#0066ff",command=self.tohome)
        searchB = Button(self.topnav, text="Search",height=3,borderwidth=4, relief="groove",bg="#0066ff",command=self.tosearch)
        profB = Button(self.topnav, text="Profile",height=3,borderwidth=4, relief="groove",bg="#9999ff")
        homeB.pack(in_=self.topnav, side=LEFT,expand=1,fill=X)
        searchB.pack(in_=self.topnav, side=LEFT,expand=1,fill=X)
        profB.pack(in_=self.topnav, side=LEFT,expand=1,fill=X)

        self.form = tk.Frame(root,relief=tk.SUNKEN, borderwidth=3)
        self.form.pack(padx=10, ipadx=10, pady=20, ipady=20)
        try:
            lbl = tk.Label(master=self.form, text="Username:").grid(row = 0, column=0, sticky="w", padx = 10, pady = 10)
            uname = tk.Label(master=self.form, width=30,text=userdata[0], font=('Times',20,'normal'), fg='red')
            uname.grid(row = 0, column=1, padx = 10, pady = 10)

            lbl = tk.Label(master=self.form, text="Password:").grid(row = 1, column=0, sticky="w", padx = 10, pady = 10)
            pwd = tk.Entry(master=self.form, width=30, font=('Times',20,'normal'), fg='red',show='*')
            pwd.insert(0,userdata[1])
            pwd.grid(row = 1, column=1, padx = 10, pady = 10)

            lbl = tk.Label(master=self.form, text="Confirm password:").grid(row = 2, column=0, sticky="w", padx = 10, pady = 10)
            cpwd = tk.Entry(master=self.form, width=30, font=('Times',20,'normal'), fg='red',show='*')
            cpwd.grid(row = 2, column=1, padx = 10, pady = 10)

            lbl = tk.Label(master=self.form, text="Full Name:").grid(row = 3, column=0, sticky="w", padx = 10, pady = 10)
            fname = tk.Entry(master=self.form, width=30, font=('Times',20,'normal'), fg='red')
            fname.insert(0,userdata[2])
            fname.grid(row = 3, column=1, padx = 10, pady = 10)

            lbl = tk.Label(master=self.form, text="Country:").grid(row = 4, column=0, sticky="w", padx = 10, pady = 10)
            country = tk.Entry(master=self.form, width=30, font=('Times',20,'normal'), fg='red')
            country.insert(0,userdata[3])
            country.grid(row = 4, column=1, padx = 10, pady = 10)

            lbl = Label(master=self.form, text="Gender:").grid(row = 5, column=0, sticky="w", padx = 10, pady = 10)
            gender = Label(master=self.form,text=userdata[4],font=('Times',15,'normal'), fg='red')
            gender.grid(row = 5, column=1,sticky="w", padx = 10, pady = 10)


            lbl = tk.Label(master=self.form, text="Age:").grid(row = 6, column=0, sticky="w", padx = 10, pady = 10)
            age = tk.Spinbox(self.form, from_=1, to=100,textvariable=DoubleVar(value=int(userdata[5])))
            age.grid(row=6, column=1,sticky="w")

        except: print('Accesed Index out of range!')

        def submit():
            if len(pwd.get())<1 or len(fname.get())<1 or len(country.get())<1 :
                lbl_result = Label(self.frm_buttons, text="All fields are mandatory!",wraplength=300)
                lbl_result.pack(side=tk.LEFT,ipadx=10)
                self.frm_buttons.after(2000, lbl_result.destroy)
                return
            if cpwd.get()!=pwd.get():
                lbl_result = Label(self.frm_buttons, text="Confirmed password does not match!",wraplength=300)
                lbl_result.pack(side=tk.LEFT,ipadx=10)
                self.frm_buttons.after(2000, lbl_result.destroy)
                return
            else:
                pass
                dataline=userdata[0]+'|'+pwd.get()+'|'+fname.get()+'|'+country.get()+'|'+userdata[4]+'|'+str(age.get())+'|0\n'
                if dataline==Profile.userD:
                    lbl_result =Label(self.frm_buttons, text="No changes made!!",wraplength=300)
                    lbl_result.pack(side=tk.LEFT,ipadx=10)
                    self.frm_buttons.after(2000, lbl_result.destroy)
                else:
                    try:
                        with open("creds.txt", "r") as f:
                            lines = f.readlines()
                        with open("creds.txt", "w") as f:
                            for line in lines:
                                if line.strip()==Profile.userD: f.write(dataline)
                                else: f.write(line)
                        lbl_result =Label(self.frm_buttons, text="Changes updated successfully!!",wraplength=300)
                        lbl_result.pack(side=tk.LEFT,ipadx=10)
                        self.frm_buttons.after(2000, lbl_result.destroy)
                    except: print('File handling error!')
                    Profile.userD=dataline

        self.frm_buttons = tk.Frame(root)
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        btn_submit = tk.Button(self.frm_buttons, text="Submit", command =submit)
        btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

    def tohome(self):
        from home import Home
        self.main_frame.destroy()
        self.form.destroy()
        self.frm_buttons.destroy()
        Home(self.root,Profile.userD,True)

    def tosearch(self):
        from search import Search
        self.main_frame.destroy()
        self.form.destroy()
        self.frm_buttons.destroy()
        Search(self.root,Profile.userD)
