from tkinter import *

def eveodd(event):
	e="even"
	o="odd"
	num1 = int(num.get())
	if num1%2==0:
		result.insert(0,e)
	else:
		result.insert(0,o)



root=Tk()
root.title("Even Odd")
Label(root,text="Enter any number").grid(row=1,column=0,sticky=W)
num = Entry(root)
num.grid(row=1,column=1,sticky=W)
eveoddbtn = Button(root,text="click on button to check even/odd")
eveoddbtn.bind("<Button-1>",eveodd)
eveoddbtn.grid(row=2,column=1,sticky=W)
Label(root,text="Answer").grid(row=3,column=0,sticky=W)
result = Entry(root)
result.grid(row=3,column=1,sticky=W)

root.mainloop()