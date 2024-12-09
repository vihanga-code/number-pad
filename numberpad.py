from  tkinter  import *
root=Tk()
root.title("number pad")
root.geometry("200x300")
nums=[[9,8,7],[6,5,4],[3,2,1],["*",0,"#"]]
root.configure(bg="skyblue")
for i in range(0,4):
    root.columnconfigure(i,weight=1,minsize=50)
    root.rowconfigure(i,weight=1,minsize=50)
    for j in range(0,3):
        frame=Frame(master=root,relief=GROOVE,borderwidth=1)
        frame.grid(row=i,column=j)
        label=Label(master=frame,text=nums[i][j],bg="white")
        label.pack(padx=4,pady=5)
root.mainloop()        
