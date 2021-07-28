import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image

class Search:
    userdata=''
    def __init__(self,root,userdata):
        Search.userdata=userdata
        self.call(root)

    def call(self,root):
        self.root=root
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=1)
        self.my_canvas = Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.my_scrollbar = tk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=BOTH)
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all")))

        self.back = Frame(self.my_canvas)
        self.my_canvas.create_window((0,200), window=self.back,width=self.root.winfo_screenwidth()-20,height=3050)

        self.topnav=Frame(self.my_canvas)
        self.topnav.pack(side=TOP,fill=X)
        homeB = Button(self.topnav, text="Home",height=3,borderwidth=4, relief="groove",bg="#0066ff",command=self.tohome)
        searchB = Button(self.topnav, text="Search",height=3,borderwidth=4, relief="groove",bg="#9999ff")
        profB = Button(self.topnav, text="Profile",height=3,borderwidth=4, relief="groove",bg="#0066ff",command=self.toprofile)
        homeB.pack(in_=self.topnav, side=LEFT,expand=1,fill=X)
        searchB.pack(in_=self.topnav, side=LEFT,expand=1,fill=X)
        profB.pack(in_=self.topnav, side=LEFT,expand=1,fill=X)

        ya=1
        self.center=Frame(self.back)
        self.center.pack(side=TOP,fill=X)
        try:
            Search.bg=ImageTk.PhotoImage(Image.open("appimages/rbooksbg.png"))
            label1 = Label( self.center, image = Search.bg)
            label1.place(x = 0, y = 0)
        except: print('Error in opening background image.')
        top5=tk.Label(self.center,text="OUR COLLECTION",width=90,borderwidth=2,font=('Cambria',20,'bold'),relief=RAISED,bg="#8f241d")
        top5.grid(row=0,column=1,pady=(110,0))
        books=self.getallbooks()
        idx=0
        for x in range(len(books)):
            w=books[x].split('|')
            txt='Title: '+w[0]+'\n\nAuthor: '+w[2]+'\n\nGenre: '+w[3]
            bookB = Button(self.center, text=txt,font=('Cambria',15,'bold'),justify=LEFT,height=6,width=50,bg="#996633",wraplength=800,command = lambda idx = x: self.playit(books[idx]))
            bookB.grid(row=x+1,column=1,pady=20)

    def tohome(self):
        from home import Home
        self.main_frame.destroy()
        Home(self.root,Search.userdata,True)

    def toprofile(self):
        from profile import Profile
        self.main_frame.destroy()
        Profile(self.root,Search.userdata)

    def getallbooks(self):
        try:
            fo=open('stories/description.txt','r')
            books=[]
            for line in fo:
                if len(line)>1: books.append(line)
            return books
        except:print('File handling error (stories/description.txt)')

    def playit(self,line):
        from play import playstart
        playstart(line)
