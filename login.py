from tkinter import *
root=Tk()
root.title("login app")
root.geometry("250x300")
frame=Frame(master=root,height=200,width=360,bg="skyblue")
lbl1=Label(frame,text="full Name",bg="lavender",fg="black",width=10)
lbl2=Label(frame,text="Email Id",bg="lavender",fg="black",width=10)
lbl3=Label(frame,text="Enter password",bg="lavender",fg="black",width=10)
name_entry=Entry(frame)
Email_entry=Entry(frame)
password_entry=Entry(frame,show="*")
def display():
    name=name_entry.get()
    greet=" hey "+name
    message=" \n congradulations for your new account "
    textbox.insert(END,greet)
    textbox.insert(END,message)
textbox=Text(bg="white",fg="black") 
btn=Button(text="click me",command=display)
frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
name_entry.place(x=150,y=20)
lbl2.place(x=20,y=80)
Email_entry.place(x=150,y=80)
lbl3.place(x=20,y=140)
password_entry.place(x=150,y=140) 
btn.place(x=130,y=210)
textbox.place(y=250) 
root.mainloop()
    
    
    
