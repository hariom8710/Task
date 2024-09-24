import tkinter as tk
from tkinter import *
window=tk.Tk()
window.title("ToDoList")
window.geometry("400x650+400+100")
window.resizable(False,False)
task_list=[]

def addTask():
    task= task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n(task)")
        task_list.append(task)    
        listbox.insert(END,task)

def deleteTask():
    global task_list 
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfile:
            taskfile.write(task+"\n")
        listbox.delete(ANCHOR)    



def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt","r")as taskfile:
            tasks=taskfile.readline()
        for task in tasks:
            if task !='\n':
                task_list.append(task)    
                listbox.insert(END,task)
    except:
        file=open("tasklist.txt", "w")
        file.close()

from tkinter import PhotoImage
images_ic=PhotoImage(file="dock.png")
window.iconphoto(False,images_ic)

images_ic2=PhotoImage(file="topbar.png",height=587)
Label(window,image=images_ic2).pack()

heading=Label(window,text="All Task" ,font="arial 20 bold",fg='black',bg="white")
heading.place(x=135,y=0)

#main
from tkinter import ttk
frame= Frame(window,width=340,height=50,bg="#2B65EC")
frame.place(x=30,y=50)

task=StringVar()
task_entry=Entry(frame,width=15,font="arial 20", bd=0)
task_entry.place( x=12,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 20 bold", width=5,bg="#89FFDE",fg="#fff",bd=0, command=addTask)
button.place(x=250,y=0)

# listbox
frame1=Frame(window,bd=5,width=50,height=150 , bg="red")
frame1.place(x=29,y=100)
listbox=Listbox(frame1,font=("arial",12),width=34,height=25,bg="#FFA500",fg="white", cursor="hand2",selectbackground="#32405b")
listbox.pack(side="left",fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side="right",fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.config(command=listbox.xview)


data =openTaskFile()

#delete
delete_frame=tk.Frame(window, width=400,height=50, bg="#89FFDE")
delete_frame.pack(padx=2,pady=2)

button=Button(delete_frame, text="DELETE",width=20,height=2,bg="lightblue" ,fg="#000000",command=deleteTask)
button.place( x=120,y=5)

window.mainloop()
