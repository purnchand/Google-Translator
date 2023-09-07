from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb_sor.get()
    d=comb_dest.get()
    masg=Sor_txt.get(1.0,END)
    textget=change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)

root=Tk()
root.title("Translator")
root.geometry("500x580")
root.config(bg="Sky Blue")

lab_txt=Label(root,text="Google Translator",font=("Time New Roman",30,"bold"),bg="sky blue")
lab_txt.place(x=54,y=25,height=50,width=400)

frame=Frame(root).pack(side=BOTTOM)


lab_txt=Label(root,text="Source Text",font=("Time New Roman",15,"bold"),fg="Black")
lab_txt.place(x=150,y=100,height=25,width=200)

Sor_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("English")

button_change=Button(frame,text="Translate",relief=RAISED,command=data,font=("Time New Roman",12),fg="blue")
button_change.place(x=170,y=300,height=40,width=150)

comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("Hindi")

lab_txt=Label(root,text="Destination Text",font=("Time New Roman",15,"bold"),fg="Black")
lab_txt.place(x=150,y=370,height=25,width=200)

dest_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

root.mainloop()
