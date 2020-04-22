import grade as g
import mini as m
from tkinter import *

class Inter:
    def __init__(self,root):
        self.app=root
        self.app.geometry('300x300')
        self.app.title('Google Translate')
        self.app.resizable(0,0)
        self.app.config(bg='blue')
    
        app_name=Label(self.app,text='Main Menu',font=('arial',20),bg='green',fg='goldenrod1',height=2)
        app_name.pack(side=TOP,fill=BOTH,pady=0)
        version=Label(self.app,text='Beta',bg='green').place(x=250,y=45)
        app_name.pack(side=TOP,fill=BOTH,pady=0)
        
        frame=Frame(self.app).pack(side=BOTTOM)
        
        
        btn1=Button(frame,text='Checker',width=20,height=3,font=('arial',10,'bold'),fg='red',bg='white',activebackground='green',relief=GROOVE,command=self.newg)
        btn1.pack(side=TOP,pady=15)
        
        btn2=Button(frame,text='Translate',width=20,height=3,font=('arial',10,'bold'),fg='red',bg='white',activebackground='green',relief=GROOVE,command=self.newm)
        btn2.pack(side=TOP,pady=15)
        
    def newg(self):
        self.app.withdraw()
        self.newwindow=Toplevel()
        ob=g.Grade(self.newwindow,self.app)
        
    def newm(self):
        self.app.withdraw()
        self.newwindow=Toplevel()
        ob=m.Mini(self.newwindow,self.app)
    
        
        



root=Tk()
obj=Inter(root)
root.mainloop()
