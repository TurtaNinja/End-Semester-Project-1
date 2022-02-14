# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:27:57 2022

@author: Muhammad Talal Faiz
"""

import requests
# A module that allows sending http requests. We will use it to make the API Call.
import smtplib
#SMTP is an Application layer protocol
#smtp stands for simple mail transfer protocol -->creates client session object
#SMTPLIB USE SMTP PROTOCOL TO SEND MAIL BETWEEN EMAIL SERVERS
def fileread():
    file=open('emaillist.txt','rt')
    x=file.read()
    global emaillist
    emaillist=x.split(" ")
    if emaillist[0]=='':
        emaillist.pop(0)
    if emaillist[-1]=='':
        emaillist.pop(-1)
def SendMail():
    global server
    server=smtplib.SMTP('smtp.gmail.com',587)
    #Defining google gmail server,port number is a way to identfy a specific process to which  message on the internet or any networks arrive on the server,WE ARE CHOOSING 587 BECAUSE WE ARE USING TLS(Transport Layer Security) FOR AUTHENTICATION
    server.starttls()
    #This is to start an encrypted channel b/w gmail server and this host and to create a secure connection using TLS
    server.login('focpproject@gmail.com','room404error')
    #Logging on to the server using our credentials so that we can send gmail
    for Email in emaillist:
        server.sendmail('focpproject@gmail.com',Email,Messsage)
def GetWeatherDataDaily():
    lat="33.684422"
    lon="73.047882"
    api="https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=minutely,alerts,hourly&appid=968e39853093a073483c700d3a991167"
    #This is the URL for retrieving data
    global json_WeatherData
    json_WeatherData= requests.get(api).json()
    #Using requests module to send http request with above URL to retrieve data in JSON Format
    #JSON is a format for storing and sending data from a server to a webpage and retrieving it. JSON format has same syntax as that used for creating JavaScriptObjects
    global ForecastedWeather
    ForecastedWeather=json_WeatherData["daily"][0]["weather"][0]["main"]
    global Precipitation
    Precipitation=json_WeatherData["daily"][0]["pop"]
    global Description
    Description=json_WeatherData["daily"][0]["weather"][0]["description"]
def Message():
    global Messsage
    if ForecastedWeather in ["Rain","Drizzle","Snow","Thunderstorm"]:
        Messsage=f"Don't forget to take your Umbrella with you !!\nThe chances of {ForecastedWeather} are {int(Precipitation*100)}%"
       
    elif ForecastedWeather=="Clouds" and Precipitation>0.4:
        Messsage=f"Don't forget to take your umbrella with you as it is Cloudy Today and chances of rain are {int(Precipitation*100)}%"
    elif ForecastedWeather=="Clouds" and Precipitation<0.4:
        Messsage="It is Cloudy Today.\nThere is no chance of rain. Enjoy !!"
    else:
        Messsage="The weather is Clear Today.\nEnjoy !!"
        
GetWeatherDataDaily()
Message()
fileread()
SendMail()

