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
	import subprocess
	subprocess.run([sys.executable,"-m pip install requests"])
	subprocess.run([sys.executable,"-m pip install tkinter"])
	import requests
	from tkinter import *
	from tkinter import ttk
	from tkinter import messagebox

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
		print("Your password is in the list of worst passwords\nIt is recommended you change it")
	else:
		print("Your password is not in the list of worst passwords\nHowever, you still should enable Multi Factor Authentication on all accounts and not reuse your password across accounts")


# get the passwords and words
words = requests.get(expand_url("data/words.txt")).text.split("\n")
worstPass = requests.get(expand_url("data/worst_password.txt")).text.split("\n")


passwd = ttk.Entry(root, textvariable=userP, show="*").grid()
button = ttk.Button(root, text='Check', command=check_p).grid()

root.title("Check your password")
root.mainloop()

