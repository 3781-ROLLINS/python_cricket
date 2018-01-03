from tkinter import *
import tkinter.messagebox
import pymysql
import random

def signup():
	firstname = fname.get()
	lastname = lname.get()
	mobile = mob.get()
	email = em.get()
	username = user.get()
	password = passw.get()
	repass = rpass.get()

	Label(frame1,text="Account Created Successfully!!",fg="green").grid()
	con = pymysql.connect(host="localhost",user="root",password="",db="python_test")
	a = con.cursor() 
	a.execute('''INSERT INTO signin(firstname,lastname,mobile,email,username,password,repassword) values(%s,%s,%s,%s,%s,%s,%s)''',(firstname,lastname,mobile,email,username,password,repass))
	con.commit()
	con.close()
	Button(frame1, text="Click here to Login",command=lambda:raise_frame(frame2)).grid()

def login():
	user1 = username1.get()
	pwd1= password1.get()
	#database connection
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

		if user1==u and pwd1==p:
			flag = 1;
			break;
		else:
			flag=0;

	if flag==1:
		raise_frame(frame3)
		Label(frame3,text="Welcome %s To Your Dashboard!" % user1).grid(row=0,column=1,padx=10,pady=10)
	else:
		#print("Failure")
		tkinter.messagebox.showinfo('Warning','Invalid Credentials')

	con.commit()
	con.close()

def register():
	raise_frame(frame4)
	Label(frame4,text="Register teams").grid(row=0,column=0,padx=10,pady=10)

def reg_teams():
	team_name = tn.get()
	P1=p1.get()
	P2=p2.get()
	P3=p3.get()
	P4=p4.get()
	P5=p5.get()
	P6=p6.get()
	P7=p7.get()
	P8=p8.get()
	P9=p9.get()
	P10=p10.get()
	P11=p11.get()
	con = pymysql.connect(host="localhost",user="root",password="",db="python_test")
	a = con.cursor() 
	a.execute('''INSERT INTO teams(team_name,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(team_name,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11))
	#print("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" %(team_name,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11))
	con.commit()
	con.close()

def matchup():
	#database connection
	con=pymysql.connect(host="localhost",user="root",password="",db="python_test")
	#cursor creation
	a = con.cursor()

	#query exection
	a.execute("SELECT * from teams")

	#fetch records form db
	rows = a.fetchall()
	mylist = []
	for x in rows:
		t = x[0]
		mylist.append(t)
	
	rv1 = random.choice(mylist)
	rv2 = random.choice(mylist)
	if(rv1!=rv2):
		newlist = [rv1,rv2]
		print(newlist)
	raise_frame(frame5)
	
	t1 = str(rv1)
	t2 = str(rv2)
	if(t1!=t2):
		team1.delete(0,"end")
		team1.insert(0,t1)
		team2.delete(0,"end")
		team2.insert(0,t2)
	else:
		matchup()
	
	t = Button(frame5,text="TOSS")
	t.bind("<Button-1>",toss)
	t.grid(row=7,column=0,pady=10,padx=10)
def selection():
	a = Lb.curselection()
	for i in a:
		print(Lb.get(i))
	start_match = Button(frame5,text="Start Match",command=match).grid(row=9,column=0,padx=10,pady=10)

#*********************************Frame 6*****************************
def match():
	raise_frame(frame6)

def toss(event):
	coin_raise=["H","T"]
	res = random.choice(coin_raise)
	coin_res = Entry(frame5)
	coin_res.grid(row=7,column=1,pady=10,padx=10)
	coin_res.delete(0,"end")
	coin_res.insert(0,res)

def raise_frame(frame):
	frame.tkraise()


root=Tk()
#root.geometry("1080x720")
root.title("DIGITAL SCORE BOARD")
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
frame4=Frame(root)
frame5=Frame(root)
frame6=Frame(root)
for frame in (frame1,frame2,frame3,frame4,frame5,frame6):
	frame.grid(row=0,column=0,sticky=N+S+E+W)

#*************************Create Account*************************
Label(frame1,text="Create Account",bg="green",fg="white",font="72",height="2",width="50",padx=30).grid(row=0,column=0,columnspan=2,sticky=E,padx=10,pady=10)

#Create entry for first name
Label(frame1,text="First Name: ").grid(row=12,column=0,sticky=W,padx=10,pady=10)
fname=StringVar()
firstname = Entry(frame1,width=35,textvariable=fname).grid(row=12,column=1,sticky=W,padx=10,pady=10)

#Create entry for last name
Label(frame1,text="Last Name: ").grid(row=13,column=0,sticky=W,padx=10,pady=10)
lname=StringVar()
lastname = Entry(frame1,width=35,textvariable=lname).grid(row=13,column=1,sticky=W,padx=10,pady=10)

#Create entry for mobile number
Label(frame1,text="Mobile Number").grid(row=14,column=0,sticky=W,padx=10,pady=10)
mob=StringVar()
mobile = Entry(frame1,width=35,textvariable=mob).grid(row=14,column=1,sticky=W,padx=10,pady=10)

#Create entry for email_id
Label(frame1,text="Email-ID").grid(row=15,column=0,sticky=W,padx=10,pady=10)
em=StringVar()
email = Entry(frame1,width=35,textvariable=em).grid(row=15,column=1,sticky=W,padx=10,pady=10)

#Create entry for username
Label(frame1,text="Username").grid(row=16,column=0,sticky=W,padx=10,pady=10)
user=StringVar()
username = Entry(frame1,width=35,textvariable=user).grid(row=16,column=1,sticky=W,padx=10,pady=10)

#Create entry for password
Label(frame1,text="Password").grid(row=17,column=0,sticky=W,padx=10,pady=10)
passw=StringVar()
password = Entry(frame1,width=35,textvariable=passw).grid(row=17,column=1,sticky=W,padx=10,pady=10)

#Create entry for Re-enter password
Label(frame1,text="Re-enter Password").grid(row=18,column=0,sticky=W,padx=10,pady=10)
rpass=StringVar()
repass = Entry(frame1,width=35,textvariable=rpass).grid(row=18,column=1,sticky=W,padx=10,pady=10)

#Signin Button
signin = Button(frame1,text="Signin",command=signup)
signin.grid(row=19,column=1,sticky=W,padx=10,pady=10)

Label(frame1,text="already have account Click Login",fg="red").grid(row=19,column=3,sticky=W,pady=10,padx=10)
Button(frame1,text="Login",command=lambda:raise_frame(frame2)).grid(row=19,column=4,sticky=W,padx=10,pady=10)


#*****************************Login Form**********************************
Button(frame2,text="<-Back",command=lambda:raise_frame(frame1)).grid(row=1,column=0,padx=10,pady=10)
Label(frame2,text="Login").grid(row=5,column=0,columnspan=2,padx=10,pady=10)

Label(frame2,text="Username").grid(row=12,column=0,sticky=W,padx=14)
username1=StringVar()
user1=Entry(frame2,width=35,textvariable=username1).grid(row=12,column=1,sticky=E,pady=14)

Label(frame2,text="Password").grid(row=13,column=0,sticky=W,padx=14)
password1=StringVar()
pwd1=Entry(frame2,width=35,show="*",textvariable=password1).grid(row=13,column=1,sticky=E,pady=14)

button = Button(frame2,text="Login",command=login).grid(row=14,sticky=W,padx=14)
Label(frame2,text="Don't have account Click 'Create Account'",fg="red").grid(row=14,column=1,sticky=W,pady=10,padx=10)
Button(frame2,text="Create Account",command=lambda:raise_frame(frame1)).grid(row=14,column=2,sticky=W,padx=10,pady=10)


#**************************DASHBOARD*****************************

Button(frame3,text="Regsiter Teams",command=register).grid(row=2,column=2,pady=10,padx=10)
Button(frame3,text="Team Matchups",command=matchup).grid(row=2,column=4,pady=10,padx=10)
Button(frame3,text="Logout",command=lambda:raise_frame(frame1)).grid(row=2,column=5,padx=10,pady=10)

#*************************Team Registeration***********************
Button(frame4,text="<-Back",command=lambda:raise_frame(frame3)).grid(row=1,column=0,padx=10,pady=10)
Label(frame4,text="Team Name:").grid(row=5,column=0,padx=10,pady=10)
tn=StringVar()
team_name=Entry(frame4,textvariable=tn).grid(row=5,column=1,padx=10,pady=10)

Label(frame4,text="Player 1:").grid(row=5,column=3,padx=10,pady=10)
p1=StringVar()
P1=Entry(frame4,textvariable=p1).grid(row=5,column=4,padx=10,pady=10)

Label(frame4,text="Player 2:").grid(row=6,column=0,padx=10,pady=10)
p2=StringVar()
P2=Entry(frame4,textvariable=p2).grid(row=6,column=1,padx=10,pady=10)

Label(frame4,text="Player 3:").grid(row=6,column=3,padx=10,pady=10)
p3=StringVar()
P3=Entry(frame4,textvariable=p3).grid(row=6,column=4,padx=10,pady=10)
	
Label(frame4,text="Player 4:").grid(row=7,column=0,padx=10,pady=10)
p4=StringVar()
P4=Entry(frame4,textvariable=p4).grid(row=7,column=1,padx=10,pady=10)

Label(frame4,text="Player 5:").grid(row=7,column=3,padx=10,pady=10)
p5=StringVar()
P5=Entry(frame4,textvariable=p5).grid(row=7,column=4,padx=10,pady=10)
	
Label(frame4,text="Player 6:").grid(row=8,column=0,padx=10,pady=10)
p6=StringVar()
P6=Entry(frame4,textvariable=p6).grid(row=8,column=1,padx=10,pady=10)

Label(frame4,text="Player 7:").grid(row=8,column=3,padx=10,pady=10)
p7=StringVar()
P7=Entry(frame4,textvariable=p7).grid(row=8,column=4,padx=10,pady=10)

Label(frame4,text="Player 8:").grid(row=9,column=0,padx=10,pady=10)
p8=StringVar()
P8=Entry(frame4,textvariable=p8).grid(row=9,column=1,padx=10,pady=10)
	
Label(frame4,text="Player 9:").grid(row=9,column=3,padx=10,pady=10)
p9=StringVar()
P9=Entry(frame4,textvariable=p9).grid(row=9,column=4,padx=10,pady=10)
	
Label(frame4,text="Player 10:").grid(row=10,column=0,padx=10,pady=10)
p10=StringVar()
P10=Entry(frame4,textvariable=p10).grid(row=10,column=1,padx=10,pady=10)
	
Label(frame4,text="Player 11:").grid(row=10,column=3,padx=10,pady=10)
p11=StringVar()
P11=Entry(frame4,textvariable=p11).grid(row=10,column=4,padx=10,pady=10)

reg=Button(frame4,text="Register",command=reg_teams).grid(row=11,column=0,padx=10,pady=10)

#**************************Random Teams Matchups******************************
Button(frame5,text="<-Back",command=lambda:raise_frame(frame3)).grid(row=1,column=0,padx=10,pady=10)
Label(frame5,text="Team 1").grid(row=3,column=0,pady=10,padx=10)
team1 = Entry(frame5)
team1.grid(row=3,column=1,pady=10,padx=10)
Label(frame5,text="Team 2").grid(row=5,column=0,pady=10,padx=10)
team2 = Entry(frame5)
team2.grid(row=5,column=1,pady=10,padx=10)
win = Entry(frame5)
win.grid(row=4,column=2,pady=10,padx=10)
t = Button(frame5,text="TOSS")
t.bind("<Button-1>",toss)
t.grid(row=7,column=0,pady=10,padx=10)

Lb = Listbox(frame5,selectmode=EXTENDED)
b = Button(frame5,text="Click Me",command=selection)
m1 = team1.get()
m2 = team2.get()
Lb.insert(1,"team1")
Lb.insert(2,"team2")
Lb.grid(row=8,column=0,padx=10,pady=10)
b.grid(row=8,column=1,padx=10,pady=10)

#**************************************************************************
raise_frame(frame1)
root.mainloop()