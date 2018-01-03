from tkinter import *

root = Tk()
root.title("Login")
root.geometry("1080x720")
Label(root,text="Institute Management System",fg="blue").grid(row=0,column=150,padx=10,pady=10)
frame=Frame(root).grid()

Label(frame,text="Username").grid(row=4,column=10,sticky=W,padx=10,pady=10)
username=Entry(frame).grid(row=4,column=11,sticky=W,padx=10,pady=10)
Label(frame,text="Password").grid(row=5,column=10,sticky=W,padx=10,pady=10)
password=Entry(frame).grid(row=5,column=11,sticky=W,padx=10,pady=10)
logbtn=Button(root,text="Login").grid(row=6,column=1)
root.mainloop()