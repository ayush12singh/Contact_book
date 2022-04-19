from ssqqll import contact
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title("Contact Book")
root.geometry('720x460+300+100')
root.configure(background="floral white")
root.resizable(0,0)
root.iconbitmap("D:\iconfinder_book_note_paper_school_2824439_chl_icon.ico") 
root.maxsize(720,460)
obj=contact()
name1=StringVar()
mail1=StringVar()
occ1=StringVar()
phone1=StringVar()
I=IntVar()
#INPUT
def add():

    def input():
        m=messagebox.askquestion("SUBMIT", "Are you sure?",parent=ad)
   
        if(m=="yes"):
         N=d1.get()
         P=d2.get()
         O=d3.get()
         E=d4.get()
         if N=="" or P=="" or O=="" or E=="":
           messagebox.showwarning("WARNING","Please Fill All Details",parent=ad)
         I=int(d5.get())
         d1.delete(0,END)
         d2.delete(0,END)
         d3.delete(0,END)
         d4.delete(0,END)
         d5.delete(0,END)
         
         obj.inser_in(I,N,P,O,E)
        else:
         d1.delete(0,END)
         d2.delete(0,END)
         d3.delete(0,END)
         d4.delete(0,END)
         d5.delete(0,END)        
    ad=Toplevel(root)
    ad.title("Add a Contact")
    ad.configure(background="floral white")
    ad.iconbitmap("D:\iconfinder_book_note_paper_school_2824439_chl_icon.ico") 
    ad.geometry('440x300+400+200')
    ad.resizable(0,0)
    l1=Label(ad,text="Enter Name :",font = ("Impact 15")).place(x=50,y=60)
    l2=Label(ad,text="Enter Phone no :",font = ("Impact 15")).place(x=50,y=100)
    l3=Label(ad,text="Enter Occupation",font = ("Impact 15")).place(x=50,y=140)
    l4=Label(ad,text="Enter EmaiID :",font = ("Impact 15")).place(x=50,y=180)
    l5=Label(ad,text="Enter ID :",font = ("Impact 15")).place(x=50,y=220)
    b1=Button(ad,text="Submit",command=input,font = ("Impact 15")).pack(side=BOTTOM)
    d1=Entry(ad)
    d1.place(x=200,y=65)
    d2=Entry(ad)
    d2.place(x=200,y=105)
    d3=Entry(ad,)
    d3.place(x=200,y=145)
    d4=Entry(ad)
    d4.place(x=200,y=185)
    d5=Entry(ad)
    d5.place(x=200,y=225)

#UPDATION
def update():
    ud=Toplevel(root)
    ud.title("Updation")
    ud.configure(background="floral white")
    ud.iconbitmap("D:\iconfinder_book_note_paper_school_2824439_chl_icon.ico") 
    ud.geometry('440x300+400+200')
    ud.resizable(0,0)
    def u():
         l2=Label(ud,text="Enter New Details",bd=1,relief=SOLID,font = ("Impact 15")).place(x=0,y=75)
         l3=Label(ud,text=" Name :",font = ("Impact 15")).place(x=0,y=110)
         l4=Label(ud,text="Phone no:",font = ("Impact 15 ")).place(x=0,y=150)
         l5=Label(ud,text="Occupation :",font = ("Impact 15 ")).place(x=0,y=190)
         l6=Label(ud,text="EmaiID :",font = ("Impact 15 ")).place(x=0,y=230)
         
         d1=Entry(ud)
         d1.place(x=140,y=120)
         d2=Entry(ud)
         d2.place(x=140,y=160)
         d3=Entry(ud)
         d3.place(x=140,y=200)
         d4=Entry(ud)
         d4.place(x=140,y=240)  
         def up(): 

          m=messagebox.askquestion("UPDATE", "Are you sure?",parent=ud)
          if(m=="yes"): 
         
           I=int(d.get())
           N=d1.get()
           P=d2.get()
           O=d3.get()
           E=d4.get()
           if N=="" or P=="" or O=="" or E=="":
            messagebox.showwarning("WARNING","Please Fill All Details",parent=ud)
           
           d.delete(0,END)
           d1.delete(0,END)
           d2.delete(0,END)
           d3.delete(0,END)
           d4.delete(0,END)
           obj.updatesql(I,N,P,O,E)       
         
          else:
           d1.delete(0,END)
           d2.delete(0,END)
           d3.delete(0,END)
           d4.delete(0,END)
           d.delete(0,END) 
         b1=Button(ud,text="UPDATE",font = ('Impact',12),command=up).pack(side=BOTTOM)
    #print(name1.get()+phone1.get()+occ1.get()+mail1.get()) 
    l1=Label(ud,text="Enter ID that has to be updated ",borderwidth=2,relief=RIDGE,font = ("Impact 15")).pack()
    d=Entry(ud)
    d.pack()
    B1=Button(ud,text="SUBMIT",font = ("Impact 8"),command=u).place(x=350,y=30)
    
#DELETION       
def delete():
    def ss():
       
       m=messagebox.askquestion("DELETE", "Are you sure?")
       if(m=="yes"): 
        if(e1.get()==""):
         messagebox.showwarning("WARNING","Please Enter A ID",parent= dd)
        num=int(e1.get())
        e1.delete(0,END)
        print(num)
       else:
        e1.delete(0,END)
    dd=Toplevel(root)
    dd.title("Deletion")
    dd.configure(background="floral white")
    dd.iconbitmap("D:\iconfinder_book_note_paper_school_2824439_chl_icon.ico") 
    dd.geometry('440x300+400+300')
    l1=Label(dd,text="Enter ID of contact that has to be deleted",borderwidth=2,relief=RIDGE,font = ("Impact 15")).pack()
    e1=Entry(dd)
    e1.pack()
    d=Button(dd,text="SUBMIT",command=ss,font = ("Impact 13")).pack()
#CLEAR CONTACTS
def clear():
    m=messagebox.askquestion("CLEAR CONTACTS","ARE YOU SURE ?")
    if(m=="yes"):
        obj.clearall()
def show():
    rt=Tk()
    rt.iconbitmap("D:\iconfinder_book_note_paper_school_2824439_chl_icon.ico") 
    rt.configure(background='DarkSeaGreen3')
    rt.geometry("1000x400+250+200")
    l1=Label(rt,text="RECORDS",fg="black",relief=GROOVE,font=("Impact 20"),bg="SlateGray3",borderwidth=1).pack()
    t=ttk.Treeview(rt,selectmode=BROWSE)
    t['columns']=(1,2,3,4,5)
    t['show']="headings"
    t.column("1",width=60,anchor='c')
    t.column("2",anchor='w')
    t.column("3",anchor='w')
    t.column("4",anchor='w')
    t.column("5",anchor='w')
    t.pack( )
    a=obj.fetch()
    t.heading(1,text="USER_ID")
    t.heading(2,text="USERNAME")
    t.heading(3,text="PHONE")
    t.heading(4,text="OCCUPATION")
    t.heading(5,text="EMAIL")
    for i in a:
         t.insert('','end',values=(i))
    rt.mainloop()
     
head=Label(root,text="CONTACT BOOK ",fg="black",relief=GROOVE,font=("Impact 30"),bg="cornsilk3",bd=12,borderwidth=10)
head.pack(side=TOP)
l1=Label(root,text="1) ADD A NEW CONTACT",bg="cornsilk3",font = ('Impact',12)).place(x=0,y=90)
l2=Label(root,text="2) UPDATE A CONTACT",bg="cornsilk3",font = ('Impact',12)).place(x=0,y=130)
l3=Label(root,text="3) SHOW ALL CONTACTS",bg="cornsilk3",font = ('Impact',12)).place(x=0,y=170)
l4=Label(root,text="4) DELETE A CONTACT",bg="cornsilk3",font = ('Impact',12)).place(x=0,y=210)
l5=Label(root,text="5) DELETE ALL CONTACTS",bg="cornsilk3",font = ('Impact',12)).place(x=0,y=250)
b1=Button(root,text="ADD",activebackground="grey",borderwidth=2,relief=RIDGE,command=add,font = (' Meiryo 10 bold')).place(x=158,y=90)
b2=Button(root,text="UPDATE",activebackground="grey",borderwidth=2,relief=RIDGE,command=update,font = (' Meiryo 10 bold')).place(x=158,y=130)
b3=Button(root,text="SHOW",activebackground="grey",borderwidth=2,relief=RIDGE,command=show,font = (' Meiryo 10 bold')).place(x=158,y=170)
b4=Button(root,text="DELETE",activebackground="grey",borderwidth=2,relief=RIDGE,command=delete,font = (' Meiryo 10 bold')).place(x=158,y=210)
b5=Button(root,text="CLEAR",activebackground="grey",borderwidth=2,relief=RIDGE,command=clear,font = (' Meiryo 10 bold')).place(x=158,y=250)
e=Button(root,text="EXIT" ,padx=20,pady=1,bd=5,activebackground="dark grey",font=("Impact 15"),command=root.destroy).pack(side=BOTTOM)



root.mainloop()