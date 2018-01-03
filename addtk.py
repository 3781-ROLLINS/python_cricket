from tkinter import *

def add(event):
	num1 = int(num1Entry.get())
	num2 = int(num2Entry.get())

	sum = num1 + num2

	result.delete(0,"end")
	result.insert(0,sum)


def sub(event):
	num1 = int(num1Entry.get())
	num2 = int(num2Entry.get())

	sum = num1 - num2

	result.delete(0,"end")
	result.insert(0,sum)


def mul(event):
	num1 = int(num1Entry.get())
	num2 = int(num2Entry.get())

	sum = num1 * num2

	result.delete(0,"end")
	result.insert(0,sum)

def div(event):
	num1 = int(num1Entry.get())
	num2 = int(num2Entry.get())

	sum = num1 / num2

	result.delete(0,"end")
	result.insert(0,sum)

root=Tk()
root.title("Arithmatic Operations")

frame = Frame(root).grid()

Label(frame,text="Enter First Number").grid(row=0,column=0,sticky=W,padx=14)
num1Entry = Entry(frame)
num1Entry.grid(row=0,column=1,sticky=W)

Label(frame,text="Enter Second Number").grid(row=1,column=0,sticky=W,padx=14)
num2Entry = Entry(frame)
num2Entry.grid(row=1,column=1,sticky=W)

Label(frame,text="Answer is :").grid(row=2,column=0,sticky=W,padx=14)
result = Entry(frame)
result.grid(row=2,column=1,sticky=W)

addbtn = Button(frame,text="Click here to add")
addbtn.bind("<Button-1>",add)
addbtn.grid(row=4,column=0,sticky=W,padx=14,pady=10)

subbtn = Button(frame,text="Click here to sub")
subbtn.bind("<Button-1>",sub)
subbtn.grid(row=4,column=1,sticky=W,padx=14,pady=10)

mulbtn = Button(frame,text="Click here to mul")
mulbtn.bind("<Button-1>",mul)
mulbtn.grid(row=5,column=0,sticky=W,padx=14,pady=10)

divbtn = Button(frame,text="Click here to div")
divbtn.bind("<Button-1>",div)
divbtn.grid(row=5,column=1,sticky=W,padx=14,pady=10)

root.mainloop()
