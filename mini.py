from tkinter import *
from tkinter import ttk
from methods import Mytranslator


class Mini:
    def __init__(self,root,oldmaster):
        self.app=root
        self.app.geometry('350x520')
        self.app.title('Google Translate')
        self.app.resizable(0,0)
        self.app.config(bg='blue')
        
        app_name=Label(self.app,text='Google Translate',font=('arial',20),bg='green',fg='goldenrod1',height=2)
        app_name.pack(side=TOP,fill=BOTH,pady=0)
        version=Label(self.app,text='Beta',bg='green').place(x=250,y=45)
        app_name.pack(side=TOP,fill=BOTH,pady=0)
        
        frame=Frame(self.app).pack(side=BOTTOM)
        
        self.source_text=Text(frame,font=('arial',10),height=11,wrap=WORD)
        self.source_text.pack(side=TOP,padx=5,pady=5)
        
        transbtn=Button(frame,text='Translate',font=('arial',10,'bold'),fg='red',bg='white',activebackground='green',relief=GROOVE,command=self.get)
        transbtn.pack(side=TOP,pady=15)
        
        lan=Mytranslator().langs
        
        self.srclang=ttk.Combobox(frame,values=lan,width=10)
        self.srclang.place(x=30,y=280)
        self.srclang.set("english")
        
        self.deslang=ttk.Combobox(frame,values=lan,width=10)
        self.deslang.place(x=240,y=280)
        self.deslang.set("hindi")
        
        
        self.des_text=Text(frame,font=('arial',10),height=12,wrap=WORD)
        self.des_text.pack(side=BOTTOM,padx=5,pady=5)
        
    def get(self):
        s=self.srclang.get()
        d=self.deslang.get()
        message=self.source_text.get(1.0,END)
        translator=Mytranslator()
        text=translator.run(txt=message,src=s,dest=d)
        self.des_text.delete(1.0,END)
        self.des_text.insert(END,text)

if __name__=="__main__":
    root = Tk()
    obj = Mini(root,oldmaster=None)
    root.mainloop()