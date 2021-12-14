from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql

def registation():
	# registation database connect 
	def action():
		if first_name.get()=="" or last_name.get()=="" or email.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = winregistation)
		elif password.get() != very_pass.get():
			messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winregistation)
		else:
			try:
				con = pymysql.connect(host="localhost",user="root",password="",database="myapp")
				print(con)
				cur = con.cursor()
				cur.execute("select * from user_information where username=%s",user_name.get())
				row = cur.fetchone()
				if row!=None:
					messagebox.showerror("Error" , "User Name Already Exits", parent = winregistation)
				else:
					cur.execute("insert into user_information(first_name,last_name,email,username,password) \
						         values(%s,%s,%s,%s,%s)",
						(
						first_name.get(),
						last_name.get(),
						email.get(),
						user_name.get(),
						password.get()
						))
					con.commit()
					con.close()
					messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winregistation)
					clear()
					#switch()
				
			except Exception as es:
				messagebox.showerror("Error" , f"Error Due to : {str(es)}", parent = winregistation)

	# close registation function			
	#def switch():
		#winregistation.destroy()

	# clear data function
	def clear():
		first_name.delete(0,END)
		last_name.delete(0,END)
		email.delete(0,END)
		user_name.delete(0,END)
		password.delete(0,END)
		very_pass.delete(0,END)


	# start registation Window	

	winregistation = Tk()
	winregistation.title("My App")
	winregistation.maxsize(width=500 ,  height=600)
	winregistation.minsize(width=500 ,  height=600)


	#heading label
	heading = Label(winregistation , text = "Registation" , font = 'Verdana 20 bold')
	heading.place(x=80 , y=60)

	# form data label
	first_name = Label(winregistation, text= "First Name :" , font='Verdana 10 bold')
	first_name.place(x=80,y=130)

	last_name = Label(winregistation, text= "Last Name :" , font='Verdana 10 bold')
	last_name.place(x=80,y=160)

	email = Label(winregistation, text= "Email :" , font='Verdana 10 bold')
	email.place(x=80,y=190)

	user_name = Label(winregistation, text= "User Name :" , font='Verdana 10 bold')
	user_name.place(x=80,y=220)

	password = Label(winregistation, text= "Password :" , font='Verdana 10 bold')
	password.place(x=80,y=250)

	very_pass = Label(winregistation, text= "Verify Password:" , font='Verdana 10 bold')
	very_pass.place(x=80,y=280)

	# Entry Box ------------------------------------------------------------------

	first_name = StringVar()
	last_name = StringVar()
	email = StringVar()
	user_name = StringVar()
	password = StringVar()
	very_pass = StringVar()


	first_name = Entry(winregistation, width=40 , textvariable = first_name)
	first_name.place(x=200 , y=133)


	
	last_name = Entry(winregistation, width=40 , textvariable = last_name)
	last_name.place(x=200 , y=163)

	
	email = Entry(winregistation, width=40, textvariable= email)
	email.place(x=200 , y=193)

	
	user_name = Entry(winregistation, width=40,textvariable = user_name)
	user_name.place(x=200 , y=223)

	
	password = Entry(winregistation, width=40, textvariable = password)
	password.place(x=200 , y=253)

	
	very_pass= Entry(winregistation, width=40 ,show="*" , textvariable = very_pass)
	very_pass.place(x=200 , y=283)


	# button login and clear

	btn_registation = Button(winregistation, text = "Registation" ,font='Verdana 10 bold', command = action)
	btn_registation.place(x=200, y=313)


	btn_login = Button(winregistation, text = "Clear" ,font='Verdana 10 bold' , command = clear)
	btn_login.place(x=300, y=313)


	winregistation.mainloop()

registation()
