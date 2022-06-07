from tkinter import *
from tkinter import messagebox

import mysql.connector as mysql
screen = Tk()
screen.geometry("250x150")
screen.title("Player Name")

#
# def print():
#     player_name = name_e.get()
#     try:
#         con = mysql.connect(host="localhost", user="root", password="Browser$123", database="SnakeGame")
#         cursor = con.cursor()
#         cursor.execute("insert into score(SrNo,phoneno,email) values(%s,%s,%s)", (cust_name, cust_phone, cust_email))
#         messagebox.showinfo(title='Status', message='Customer added successfully!')
#         con.commit()
#         con.close()
#
#     except IndexError:
#         messagebox.showinfo(title="Error", message="Data Already Exists")
#     except Exception as e:
#         messagebox.showinfo(title="Error", message=e)
#     screen.destroy()


name = Label(text="Name :", padx=20, pady=20)
name.grid(row=1, column=1)
name_e = Entry()
name_e.grid(row=1, column=2)
play = Button(text="Play", command=print)
play.grid(row=2, column=2)








screen.mainloop()