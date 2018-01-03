from tkinter import *
def selection():
	a = Lb.curselection()
	for i in a:
		print(Lb.get(i))

root = Tk()

Lb = Listbox(root,selectmode=EXTENDED)
b = Button(root,text="Click Me",command=selection)
Lb.insert(1,"Python")
Lb.insert(2,"Java")
Lb.pack()
b.pack()
root.mainloop()