# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 11:52:57 2022

@author: Muhammad Talal Faiz
"""
def fileread():
    file=open('Emails.txt','rt')
    x=file.read()
    lis=x.split(" ")
    if lis[0]=='':
        lis.pop(0)
    print(lis)
def filewrite():
    file=open('Emails.txt','a')
    x=" "+ EmailEntry.get()
    file.write(x)
    EmailEntry.delete(0,len(EmailEntry.get()))
import tkinter as gui
window=gui.Tk()
window.title("Weather App")
window.geometry("800x500+350+190")
window.resizable(False,False)
window.iconbitmap(r'weather-app.ico')
#Creating a Canvas to Draw on
WeatherCanvas=gui.Canvas(window,width='600',height='500')
WeatherCanvas.pack(fill="both",expand="true")
#Putting Background Image
bg=gui.PhotoImage(file="BlueBackground4.png")
WeatherCanvas.create_image(0,0,image=bg,anchor='nw')
#Putting Logo
logo=gui.PhotoImage(file="weather-app.png")
WeatherCanvas.create_image(240,50,image=logo)
#fonts
WeatherFont2=('Arial',27,'bold')
WeatherFont3=('Bookman Old Style',53,'bold')
WeatherFont=('Bookman Old Style',35,'bold')
WeatherFont4=('poppins',20)
#Main heading
WeatherCanvas.create_text(440,50,text="Weather App",font=WeatherFont,fill="White")
#temperature
WeatherCanvas.create_text(310,180,text="19°C",font=WeatherFont3,fill="White")
#logo of weather
logo1=gui.PhotoImage(file="icon3.png")
WeatherCanvas.create_image(100,225,image=logo1)
#Line 
WeatherCanvas.create_text(192,225,text="|",font=('Times New Roman',180),fill='White')


WeatherCanvas.create_text(312,280,text="Clear Sky",font=WeatherFont2,fill="Black")
WeatherCanvas.create_text(392,330,text="WindSpeed: "+"20 kph  |"+"  Feels like "+"17°C",font=8)
#Putting Text
WeatherFont=('Bookman Old Style',30,'bold')
WeatherFont2=('poppins',20,'bold')
#textbox
textbox=gui.PhotoImage(file="textbox.png")
WeatherCanvas.create_image(390,405,image=textbox)
#Button and Entry
EmailEntry=gui.Entry(window,width=30,justify="center",border=0,font=('Arial',12))
WeatherCanvas.create_window(390,405,window=EmailEntry)
Subscribe=gui.Button(window,text="Subscribe !",command=filewrite,border=0,width=15,font=('Arial',12))
WeatherCanvas.create_window(390,450,window=Subscribe)
fileread()
#Image


'''
WeatherCanvas.create_text(420,50,text="Weather App",font=WeatherFont,fill="White")
#Putting Weather Data
WeatherCanvas.create_text(300,125,text="Clear Sky",font=WeatherFont2,fill="Light Green")

'''
window.mainloop() 




