from tkinter import *

root=Tk()

root.title("First Window")
root.geometry("1080x720")

app=Frame(root)
app.grid()

label=Label(app,text="This is Login Button")
label.grid()
button1=Button(app, text="Login")
button1.grid()
button2=Button(app, text="RESET")
button2.grid()
button3=Button(app, text="Create Account")
button3.grid()

root.mainloop()
