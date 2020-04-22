from tkinter import *
from tkinter import ttk
import new as n

class Grade :
    def __init__(self,app,oldmaster):
        self.app=app
        self.app.geometry('350x520')
        self.app.title('')
        self.app.resizable(0,0)
        self.app.config(bg='blue')
    
        app_name=Label(self.app,text='Google Translate',font=('arial',20),bg='green',fg='goldenrod1',height=2)
        app_name.pack(side=TOP,fill=BOTH,pady=0)
        version=Label(self.app,text='Beta',bg='green').place(x=250,y=45)
        app_name.pack(side=TOP,fill=BOTH,pady=0)
            
        frame=Frame(self.app).pack(side=BOTTOM)
            
        self.source_text=Text(frame,font=('arial',10),height=11,wrap=WORD)
        self.source_text.pack(side=TOP,padx=5,pady=5)
    
            
        transbtn=Button(frame,text='CHECK',font=('arial',10,'bold'),fg='red',bg='white',activebackground='green',relief=GROOVE,command=self.get)
        transbtn.pack(side=TOP,pady=15)
            
            
        self.des_text=Text(frame,font=('arial',10),height=12,wrap=WORD)
        self.des_text.pack(side=BOTTOM,padx=5,pady=5)
        
    def get(self):
        message=self.source_text.get(1.0,END)
        text=n.fun1(message)
        self.des_text.delete(1.0,END)
        self.des_text.insert(END,text)
        
       
        
if __name__=="__main__":
    root = Tk()
    obj = Grade(root,oldmaster=None)
    root.mainloop()
