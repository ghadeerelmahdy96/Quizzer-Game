#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:10:22 2019

@author: ghadeerelmahdy
"""
import socket
import threading as th
import time

import pickle

count =0
score =0
answer =""

questionSet = {  
                 1:["where is Alps Mountain located?","South Europe","North Europe","South Europe","West Europe","East Europe"] ,                
                 2:["what is the currency of switzerland?","Frank","Dollar","Euro","yen","Frank"] ,                
                 3:["what is the currency of Brazil?","Real","Real","Frank","Dollar","Euro"] ,
                 4:["what is the currency of south africa?","Rand","Real","Frank","Dollar","Rand"],
                 5:["500/100+20*10-30","175","220","175","100","200"],
                 6:["where is the main office of Google?","California","Florida","Washington","Texas","California"]
                 
                }     

         
def connectNewUser(c,ad):
    global score
    score =0
    rec=th.Thread(target=sendToAll,args=(c,))
    rec.start()
    while True:
        recieve(c)
             

      

        
def sendToAll(conn) :
         global answer,score
         for ques in questionSet.values(): 
           answer = ques[1]  
           data_str = pickle.dumps(ques)   
           conn.send(data_str)
           time.sleep(10) #10 second for every question
         data_s=['s',str(score)]  
         conn.send(pickle.dumps(data_s))     
           
def recieve(conn) :
     global score,answer
     data = conn.recv(500).decode('UTF-8')
     if data == answer:
      score +=1
             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket number
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #LEVEL(3LA MOSTWA EL SOCKET) , OPTION(REUSE ADDRESS), VALUE OF OPTION
host= "127.0.0.1"
port = 7000
s.bind((host,port))
s.listen(5)   
while True:
 conn,add = s.accept()     
 client=th.Thread(target= connectNewUser,args=(conn,add))
 client.start() 
 
