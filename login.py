from tkinter import *
import tkinter.messagebox
import pymysql

def login():
	user = username.get()
	pwd = password.get()

	#database connectio
	con=pymysql.connect(host="localhost",user="root",password="",db="python_test")
	#cursor creation
	a = con.cursor()

	#query exection
	a.execute("SELECT * from signin")

	#fetch records form db
	rows = a.fetchall()
	#store username and password in varaibles
	for row in rows:
		u=row[4]
		p=row[5]
	if u==user and p==pwd:
		#Label(frame,text="Login Successful....!",fg="green").grid()
		tkinter.messagebox.showinfo('Successs','Logged In Successfully')
		
	else:
		#Label(frame,text="Invalid User...!",fg="red").grid()
		tkinter.messagebox.showinfo('Warning','Invalid Credentials')

	mylist = []
	mylist.append(user)
	mylist.append(pwd)
	for x in mylist:
		print(x)
		
	con.commit()
	con.close()

root=Tk()
root.geometry("300x200")
root.title("Login Page")

frame = Frame(root).grid()
label = Label(frame,text="Username").grid(row=0,sticky=W,padx=14)
username=StringVar()
user=Entry(frame,textvariable=username).grid(row=0,column=1,sticky=E,pady=14)

label = Label(frame,text="Password").grid(row=1,sticky=W,padx=14)
password=StringVar()
pwd=Entry(frame,textvariable=password).grid(row=1,column=1,sticky=E,pady=14)

button = Button(frame,text="Login",command=login).grid(row=3,sticky=W,padx=14)

root.mainloop()