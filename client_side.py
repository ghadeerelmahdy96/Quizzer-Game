#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:22:35 2019

@author: ghadeerelmahdy
"""


import tkinter as tk
import socket
import threading as th
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host= "127.0.0.1"
port = 7000
s.connect((host,port))

windowshow = tk.Tk()
windowshow.title("client")
windowshow.geometry("400x300")


def Clicked():
    x=en.get()
    s.send(x.encode('utf8'))   
    
    

def recieveThread (s):
    while True:
      message = s.recv(500).decode("utf8")
      lbl2["text"]=message 
      
en= tk.Entry(windowshow,width=40)
en.grid(row=1,column=1) 
    
btn1 = tk.Button(windowshow,text="send",bg="blue",font=("Times", "10", "bold italic"),width=6,height=1,command = Clicked)
btn1.grid(row=2,column=0) 

lbl2=tk.Label(windowshow,bg="grey",font=("Times", "10", "bold italic"))
lbl2.grid(row=4,column=1)

rec=th.Thread(target=recieveThread,args=(s,))
rec.start()
   

windowshow.mainloop()

        
s.close() 