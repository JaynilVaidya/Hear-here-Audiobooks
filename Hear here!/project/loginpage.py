import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

class App:
    usr=""
    pwd=""
    userdata=""
    def __init__(self, root):

        root.title("Login")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background='black')

        Ulabel=tk.Label(root,text='Username',borderwidth=2,font=('Times',20,'normal'),fg='white',bg='brown')
        Ulabel.place(x=210,y=180,width=110,height=25)

        App.usr=StringVar()
        Uname=tk.Entry(root,textvariable=App.usr,borderwidth=2,font=('Times',15,'normal'),fg='blue')
        Uname.place(x=210,y=230,width=90,height=25)

        PLabel=tk.Label(root,text='Password',borderwidth=2,font=('Times',20,'normal'),fg='white',bg='brown')
        PLabel.place(x=210,y=290,width=110,height=25)

        App.pwd=StringVar()
        Pass=tk.Entry(root,textvariable=App.pwd,borderwidth=2,font=('Times',15,'normal'),fg='blue',show='*')
        Pass.place(x=210,y=340,width=90,height=25)

        button = tk.Button(root, text='Login', width=25, command=self.loggedin)
        button.place(x=210,y=380,width=70,height=25)

        button = tk.Button(root, text='Sign Up', width=25,command= self.Onclicksignup)
        button.place(x=210,y=420,width=70,height=25)


    def loggedin(self):
        if self.checkData(App.usr,App.pwd) == False:
            UserNotFound = Message( root, text='Username or Password is incorrect!',width=200,bg='green')
            UserNotFound.place(x=210,y=0,width=200)
            root.after(2000, UserNotFound.destroy)
        else:
            root.destroy()
            from home import homestart
            homestart(App.userdata)
            exit()
    def Onclicksignup(self):
        from signup import signupstart
        signupstart()

    def checkData(self,u,p):
        try:
            fp=open("creds.txt","r")
            for lines in fp:
                line=lines.split('|')
                if line[0].strip()==str(u.get()).strip() and line[1].strip()==str(p.get()).strip():
                    fp.close()
                    App.userdata=lines.strip()
                    return True
            fp.close()
        except:
            print('File handling error (creds.txt)')
            return False
        else:
            return False


if __name__ == "__main__":
    root = tk.Tk()
    try:
        bg=ImageTk.PhotoImage(Image.open("appimages/booksbg.png"))
        label1 = Label( root, image = bg)
        label1.place(x = 0, y = 0)
    except: print('Error in opening background image.')
    app = App(root)
    root.mainloop()
