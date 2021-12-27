# password-check
Because everyone's password is just 'password'

### Note:
Password-check is changing to a web-based tool at https://iam-py-test.github.io/password-check/website

### About password-check
_password-check_ is a Python tool to get the strength of a password
### Use
- Option 1:
Download and run [src/check.py](https://github.com/iam-py-test/password-check/blob/main/src/check.py) via Python for use in the terminal
- Option 2:
Download and run [src/gui_check.py](https://github.com/iam-py-test/password-check/blob/main/src/gui_check.py) via Python for a graphical interface
- Option 3 (WindowsOS only):
Download and run [gui_check.exe](https://github.com/iam-py-test/password-check/blob/main/gui_check.exe). This does not require installation of Python

#### IMPORTANT NOTE:
Windows Defender Smartscreen may block the file. It should be safe. Windows just warns about any unsigned file downloaded from the internet, and because I can not afford the time and money it takes to get a signing key, I have not signed it. <br>
If you do not trust it, read over the source code in [src/gui_check.py](https://github.com/iam-py-test/password-check/blob/main/src/gui_check.py) and compile it via Pyinstaller yourself. <br>
To continue, click _More info_: <br>
![image](https://user-images.githubusercontent.com/84232764/141490885-a89b463d-e004-4256-a944-f901026cbcd8.png) <br>
Then click _run anyway_: <br>
![image](https://user-images.githubusercontent.com/84232764/141491131-5a49736b-e4cd-4564-93bd-fbad276d6305.png) <br>
[Some antivirus/antimalware tools](https://www.virustotal.com/gui/file/c52ede3b99c7610c391fac5c89bc1883e4b3dc70228cc1b67b50db70f8a85b88?nocache=1) may flag it as malware. This is a false positive. If you do not trust it, either use the Python version, run it in a VM, or compile it yourself. 


