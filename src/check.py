# import everything we need
import os
import hashlib
import sys
import getpass
import random

# this isn't always installed
try:
	import requests
except:
	import subprocess
	subprocess.run([sys.executable,"-m pip install requests"])
	import requests

# store the user's password
upw = {}
id = random.choice(["1","2","3"]) # I have no idea if this actually improves security

# when you fork, be sure to change this
baseurl = "https://raw.githubusercontent.com/iam-py-test/password-check/main/"
def expand_url(path):
	return baseurl + path

# get the passwords and words
words = requests.get(expand_url("data/words.txt")).text.split("\n")
worstPass = requests.get(expand_url("data/worst_password.txt")).text.split("\n")

# get the user's password
upw[id] = getpass.getpass("Enter a password: ")

# check if it is in the worst passwords
if upw[id] in worstPass:
	print("Your password is in the list of worst passwords\nIt is recommended you change it")
else:
	print("Your password is not in the list of worst passwords\nHowever, you still should enable Multi Factor Authentication on all accounts and not reuse your password across accounts")

