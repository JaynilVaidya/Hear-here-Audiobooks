import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image

class Home:
    userdata=''
    def __init__(self,root,userdata,flag=False):
        Home.userdata=userdata
        self.root=root
        if flag==False:
            self.root=root
            self.root.title("Hear here")
            screenwidth = self.root.winfo_screenwidth()#1366
            screenheight = self.root.winfo_screenheight()#768
            alignstr = '%dx%d+%d+%d' % (screenwidth-20, screenheight-100,0,0)
            self.root.geometry(alignstr)
            self.root.resizable(width=False, height=False)
            self.root.configure(background='#ccffcc')
            header=tk.Label(self.root,text='HEAR here',borderwidth=2,font=('Candara',20,'bold'),relief=RAISED,bg="#996633")
            header.pack(side=TOP,fill=BOTH)
            footer = Label( self.root, text='NOW ENJOY YOUR AUDIOBOOKS IN TWO DIFFERENT VOICES',bg='black',fg='yellow').pack(side=BOTTOM,fill=X)

        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=1)
        self.my_canvas = Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.my_scrollbar = tk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=BOTH)
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all")))

        self.back = Frame(self.my_canvas)
        self.my_canvas.create_window((0,200), window=self.back,width=self.root.winfo_screenwidth()-20,height=self.root.winfo_screenheight()+350)
        self.call(self.root,self.my_canvas,self.back)

    def call(self,root,my_canvas,back):

        self.topnav=Frame(self.my_canvas)
        self.topnav.pack(side=TOP,fill=X)
        homeB = Button(self.topnav, text="Home",height=3,borderwidth=4, relief="groove",bg="#9999ff")
        searchB = Button(self.topnav, text="Search",height=3,borderwidth=4, relief="groove",bg="#0066ff",command=self.tosearch)
        profB = Button(self.topnav, text="Profile",height=3,borderwidth=4, relief="groove",bg="#0066ff",command=self.toprofile)
        homeB.pack(in_=self.topnav, side=LEFT,expand=1,fill=X)
        searchB.pack(in_=self.topnav, side=LEFT,expand=1,fill=X)
        profB.pack(in_=self.topnav, side=LEFT,expand=1,fill=X)

        ya=1
        self.center=Frame(self.back)
        self.center.pack(side=TOP,fill=X)
        try:
            self.bg=ImageTk.PhotoImage(Image.open("appimages/booksbg.png"))
            label1 = Label( self.center, image = self.bg)
            label1.place(x=0,y=0)
        except: print('Error in opening background image.')
        top5=tk.Label(self.center,text="TODAY'S TOP 5 PICKS FOR YOU",borderwidth=2,width=90,font=('Cambria',20,'bold'),relief=RAISED,bg="#8f241d")
        top5.grid(row=0,column=1,pady=(110,0))
        books=self.getbooks()
        idx=0
        for x in range(len(books)):
            w=books[x].split('|')
            txt='Title: '+w[0]+'\n\nAuthor: '+w[2]+'\n\nGenre: '+w[3]
            bookB = Button(self.center, text=txt,font=('Cambria',15,'bold'),justify=LEFT,height=6,width=50,bg="#996633",wraplength=800,command = lambda idx = x: self.playit(books[idx]))
            bookB.grid(row=x+1,column=1,pady=20)

    def tosearch(self):
        from search import Search
        self.main_frame.destroy()
        Search(self.root,Home.userdata)

    def toprofile(self):
        from profile import Profile
        self.main_frame.destroy()
        Profile(self.root,Home.userdata)

    def getbooks(self):
        import numpy as np
        try:
            lines = open('stories/description.txt','r').read().splitlines()
            arr=np.array(lines)
            return list(np.random.choice(arr, 5, replace=False))
        except: print('File handling error (stories/description.txt)')

    def playit(self,line):
        from play import playstart
        playstart(line)


def homestart(userdata):
    root = tk.Tk()
    home = Home(root,userdata)
    root.mainloop()
