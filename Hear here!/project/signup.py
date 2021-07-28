import tkinter as tk
from tkinter import *

class signup:
    def __init__(self,root2):
        self.dataline=''
        root2.title("Signup page")
        width=750
        height=550
        screenwidth = root2.winfo_screenwidth()
        screenheight = root2.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root2.geometry(alignstr)
        root2.resizable(width=False, height=False)
        root2.configure(background='grey')

        form = tk.Frame(root2,relief=tk.SUNKEN, borderwidth=3)
        form.pack(padx=10, ipadx=10, pady=20, ipady=20)

        lbl = tk.Label(master=form, text="Enter username:").grid(row = 0, column=0, sticky="w", padx = 10, pady = 10)
        uname = tk.Entry(master=form, width=30, font=('Times',20,'normal'), fg='red')
        uname.grid(row = 0, column=1, padx = 10, pady = 10)

        lbl = tk.Label(master=form, text="Enter password:").grid(row = 1, column=0, sticky="w", padx = 10, pady = 10)
        pwd = tk.Entry(master=form, width=30, font=('Times',20,'normal'), fg='red',show='*')
        pwd.grid(row = 1, column=1, padx = 10, pady = 10)

        lbl = tk.Label(master=form, text="Confirm password:").grid(row = 2, column=0, sticky="w", padx = 10, pady = 10)
        cpwd = tk.Entry(master=form, width=30, font=('Times',20,'normal'), fg='red',show='*')
        cpwd.grid(row = 2, column=1, padx = 10, pady = 10)

        lbl = tk.Label(master=form, text="Full Name:").grid(row = 3, column=0, sticky="w", padx = 10, pady = 10)
        fname = tk.Entry(master=form, width=30, font=('Times',20,'normal'), fg='red')
        fname.grid(row = 3, column=1, padx = 10, pady = 10)

        lbl = tk.Label(master=form, text="Country:").grid(row = 4, column=0, sticky="w", padx = 10, pady = 10)
        country = tk.Entry(master=form, width=30, font=('Times',20,'normal'), fg='red')
        country.grid(row = 4, column=1, padx = 10, pady = 10)

        lbl = tk.Label(master=form, text="Gender:").grid(row = 5, column=0, sticky="w", padx = 10, pady = 10)
        gen=StringVar(root2)
        gender = Radiobutton(form, text="Male", value="Male",variable=gen,tristatevalue=0)
        gender.grid(row = 5, column=1,sticky="w", padx = 10, pady = 10)
        gender = Radiobutton(form, text="Female", value="Female",variable=gen,tristatevalue=0)
        gender.grid(row = 6, column=1,sticky="w", padx = 10, pady = 10)


        lbl = tk.Label(master=form, text="Age:").grid(row = 7, column=0, sticky="w", padx = 10, pady = 10)
        age = tk.Spinbox(form, from_=1, to=100)
        age.grid(row=7, column=1,sticky="w")

        def submit():
            if len(uname.get())<1 or len(pwd.get())<1 or len(fname.get())<1 or len(country.get())<1 or len(gen.get())<1 :
                lbl_result = Label(frm_buttons, text="All fields are mandatory!",wraplength=300)
                lbl_result.pack(side=tk.LEFT,ipadx=10)
                frm_buttons.after(1500, lbl_result.destroy)
                return
            if cpwd.get()!=pwd.get():
                lbl_result = Label(frm_buttons, text="Confirmed password does not match!",wraplength=300)
                lbl_result.pack(side=tk.LEFT,ipadx=10)
                frm_buttons.after(1500, lbl_result.destroy)
                return
            fp=open('creds.txt','r')
            for line in fp:
                line=line.split('|')
                if line[0].strip()==str(uname.get()).strip():
                    fp.close()
                    lbl_result =Label(frm_buttons, text="Username already exists !",wraplength=300)
                    lbl_result.pack(side=tk.LEFT,ipadx=10)
                    frm_buttons.after(1500, lbl_result.destroy)
                    return
            else:
                fp.close()
                fp= open('creds.txt','a')
                self.dataline=uname.get()+'|'+pwd.get()+'|'+fname.get()+'|'+country.get()+'|'+gen.get()+'|'+str(age.get())+'|0\n'
                fp.write(self.dataline)
                fp.close()
                root2.destroy()

        frm_buttons = tk.Frame(root2)
        frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        btn_submit = tk.Button(frm_buttons, text="Submit", command =submit)
        btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


def signupstart():
    root2 = tk.Tk()
    app = signup(root2)
    root2.mainloop()
