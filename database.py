from cProfile import label
from logging import root
from math import expm1
import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call

import tkinter as tk


def ok():
	mysqldb = mysql.connector.connect(host="localhost", user="root", password = "" , db = "testing")
	mycursor = mysqldb.cursor()
	uname = e1.get()
	password = e2.get()



	sql = "select * from login where uname = %s and password = %s"
	mycursor.execute(sql,[(uname) , (password)])
	results = mycursor.fetchall()

	if results:
		messagebox.showinfo("","login success")
		root.destroy()
		call(["python","Main.py"])
		return True
	else:
		messagebox.showinfo("","Incorrect username and password")
		return False

root = tk.Tk()
root.title("login")
root.geometry("300x200")

global e1
global e2

Label(root, text = "username").place(x = 30,y = 50)  
Label(root, text = "password").place(x = 30, y = 90)  
  
e1 = Entry(root,width = 20)
e1.place(x = 100, y = 50)  
  
  
e2 = Entry(root, width = 20)
e2.place(x = 100, y = 90)
e2.config(show="*")
  
Button(root , text="login" , command=ok ,activebackground = "pink", activeforeground = "blue").place(x=30,y=120)

root.mainloop()  





















# label(root, text="username").place(x=10,y=10)
# label(root, text="password").place(x=10,y=40)

# e1.Entry(root)
# e1.place(x=140 , y=10)

# e2.Entry(root)
# e2.place(x=140 , y=10)
# e2.config(show="*")


# Button(root , text="Login" , command=Ok , height=3 , width=13).place(x=10,y=100)

# root.mainloop()
