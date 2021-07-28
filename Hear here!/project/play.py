import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont

class Play:
    def __init__(self,root,dataline):
        words=dataline.split('|')
        root.title("Hear here")
        alignstr = '%dx%d+%d+%d' % (root.winfo_screenwidth()-20, root.winfo_screenheight()-100,0,0)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background='#36454F')

        header=tk.Label(root,text='HEAR here',borderwidth=2,font=('Candara',20,'bold'),relief=RAISED,bg="#996633").pack(side=TOP,fill=X)

        title=tk.Label(root,text=words[0].strip(),fg = "#322e2f",font = ("Monotype Corsiva",30),borderwidth=2,relief="solid").pack(pady=20,ipady=10,ipadx=20,side=TOP)
        text="Author:"+words[2]+"\n\nGenre: "+words[3]+"\n\nPublisher's recommended age(s): "+words[4]+"\n\nHear here! Ratings: "+words[5]
        info=tk.Label(root,fg = "#a0d2eb",text=text,borderwidth=5,relief="solid",bg = "#8458B3",font = "Helvetica 16 bold italic").pack(side=LEFT)

        try:
            img = ImageTk.PhotoImage(Image.open('appimages/playbgm.png'))
            panel = Button(root, image=img,command=lambda: self.audio(dataline.split('|')[0],True))
            panel.photo = img
            panel.pack(padx=20,side=RIGHT)

            img = ImageTk.PhotoImage(Image.open('appimages/playbgf.png'))
            panel = Button(root, image=img,command=lambda: self.audio(dataline.split('|')[0],False))
            panel.photo = img
            panel.pack(padx=20,side=RIGHT)
        except: print('Error in opening background image.')

        summary=''
        try:
            for lines in open("stories/summaries/"+words[0].strip()+".txt", "r"):
                summary+=lines
        except: print('File handling error!')
        desc=tk.Message(root,text=summary,borderwidth=2,relief="solid",fg = "#9df9ef",bg = "#a28089",font = "Times 12 bold").pack(side=BOTTOM,pady=20,ipady=10,ipadx=20)
        summ=tk.Label(root,text="Summary",borderwidth=2,relief="solid",fg = "#51e2f5",bg = "#a28089",font = "Verdana 20 bold",justify = "center").pack(side=BOTTOM,ipady=10,ipadx=20)

    def audio(self,name,male):
        from pyttsx import tts
        tts(name.strip(),male)


def playstart(dline):
    root3=tk.Toplevel()
    try:
        bg = ImageTk.PhotoImage(Image.open( (dline.split('|'))[1].strip()) )
        label1 = Label( root3, image = bg)
        label1.place(x=0,y=0)
    except: print('Error in opening background image.')
    Play(root3,dline)
    root3.mainloop()
