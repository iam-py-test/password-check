"""this is a version of check.py which uses tkinter"""

# import everything we need
import os
import hashlib
import sys
import getpass
import random

# this isn't always installed
try:
	import requests
	from tkinter import *
	from tkinter import ttk
	from tkinter import messagebox
except:
	pass

root = Tk()
userP = StringVar()

# when you fork, be sure to change this
baseurl = "https://raw.githubusercontent.com/iam-py-test/password-check/main/"
def expand_url(path):
	return baseurl + path
def check_p():
	passwd = userP.get()
	# check if it is in the worst passwords
	if passwd in worstPass:
		messagebox.showinfo(title="Password check result",message="Your password is in the list of worst passwords")
	else:
		messagebox.showinfo(title="Password check result",message="Your password is not in the list of worst passwords")


# get the passwords and words
words = requests.get(expand_url("data/words.txt")).text.split("\n")
worstPass = requests.get(expand_url("data/worst_password.txt")).text.split("\n")

root.geometry("300x300")

passwd = ttk.Entry(root, textvariable=userP, show="*").pack()
button = ttk.Button(root, text='Check', command=check_p).pack()

root.title("Check your password")
root.mainloop()

