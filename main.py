import tkinter as tk
from tkinter import *
from tkinter import simpledialog   
import subprocess
import time
import webbrowser  
import os
url="https://www.youtube.com/channel/UCuafVcvdT\nEir2jaXW8hhaoQ"
os.system("service tor start")
def callback():
    webbrowser.open_new("https://www.youtube.com/channel/UCuafVcvdTEir2jaXW8hhaoQ") 
def start_proxy():
    os.system("sudo xterm -geometry 93x31+1400+900 -bg black -fg white   -e python3 /usr/local/bin/run.py &")
    
def stop_proxy():
    os.system("sudo killall xterm")
    os.system("sudo service tor stop")
    os.system("sudo bash /usr/local/bin/support.sh -c")
    os.system("sudo rm -rf /etc/resolv.conf")
    os.system("sudo cp /usr/local/bin/resolv.conf /etc/resolv.conf;exit")
def restart_proxy():
    os.system("sudo killall xterm")
    os.system("sudo service tor stop")
    os.system("sudo bash /usr/local/bin/support.sh -c")
    os.system("sudo rm -rf /etc/resolv.conf")
    os.system("sudo cp /usr/local/bin/resolv.conf /etc/resolv.conf;exit")
    os.system("sudo xterm -geometry 93x31+1400+900 -bg black -fg white   -e python3 /usr/local/bin/run.py &")
    
    
def exit_proxy():
    os.system("sudo killall xterm")
    os.system("sudo service tor stop")
    os.system("sudo bash /usr/local/bin/support.sh -c")
    os.system("sudo rm -rf /etc/resolv.conf")
    os.system("sudo cp /usr/local/bin/resolv.conf /etc/resolv.conf;exit")
    
    exit()
    
root = Tk()
root.geometry('350x350')
root.resizable(width=False, height=False)
root.wm_title("AUTOPROX")
root.configure(bg='black')
l1 = Label(root, text="AUTOPROX",font=("courier",40,"underline"))
l1.pack(padx=20,pady=10)
l1.configure(bg='black', fg='white')
button_submit = tk.Button(root, text = url,font=("courier",9,"bold"), bg='black', fg='red', command=callback)
button_submit.config(width=50, height=3)
 
button_submit.pack()                  
frame = tk.Frame(root)
frame.pack()
frame.configure(bg='black')
slogan = tk.Button(frame,
                   text="STOP",
                   command=stop_proxy, 
                    bg="black", fg='white')
slogan.pack(fill=tk.X, pady=10)

slogan = tk.Button(frame,
                   text="RESET",
                   command=restart_proxy,
                   bg="black",fg='white')
slogan.pack(fill=tk.X, pady=10)

slogan = tk.Button(frame,
                   text=" EXIT ",
                   command=exit_proxy,
                   bg="black",fg='white')
slogan.pack(fill=tk.X, pady=10)
connect = tk.Button(root,
                text="CONNECT",
                command=start_proxy,
                bg="black",fg='white')
connect.pack(pady=10)
connect.config(width=100, height=2,)
root.mainloop()


