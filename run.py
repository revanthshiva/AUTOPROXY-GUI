import os
import time
import pyfiglet
import tkinter as tk
from tkinter import *
from tkinter import simpledialog  
ROOT = tk.Tk()
ROOT.withdraw()

USERINP = simpledialog.askstring(title="AUTOPROX",prompt="Set time in seconds to change your IP : ")
int_USERINP =int(USERINP)



print("Your IP will change every" ,int_USERINP, "seconds")
os.system("bash /usr/local/bin/support.sh -t")
time.sleep(int_USERINP)
while True :
   os.system("bash /usr/local/bin/support.sh -r")
   time.sleep(int_USERINP)
root.mainloop()
   
   
