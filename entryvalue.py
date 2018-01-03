from tkinter import *

def check():
	gettxt = ment.get()
	output = Label(root,text=gettxt).grid()

root = Tk()
root.title("Entry-Box Example")
ment=StringVar()

Label(root,text="Enter the text: ",fg="red").grid(row=1,column=0,sticky=W)
mEntry = Entry(root,textvariable=ment).grid(row=1,column=1,sticky=W)
btn = Button(root,text="Click",command=check,fg="red").grid()
root.mainloop()