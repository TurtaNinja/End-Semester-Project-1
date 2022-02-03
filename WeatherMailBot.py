# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:00:30 2022

@author: Muhammad Talal Faiz
"""
import requests
# A module that allows sending http requests. We will use it to make the API Call.
#import time
#A module that allows us to manipulate time and in our case convert time given in Seconds sinche epoch to Local Time
import smtplib
#SMTP is an Application layer protocol
#smtp stands for simple mail transfer protocol -->creates client session object
#SMTPLIB USE SMTP PROTOCOL TO SEND MAIL BETWEEN EMAIL SERVERS
def SendMail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    #Defining google gmail server,port number is a way to identfy a specific process to which  message on the internet or any networks arrive on the server,WE ARE CHOOSING 587 BECAUSE WE ARE USING TLS(Transport Layer Security) FOR AUTHENTICATION
    server.starttls()
    #This is to start an encrypted channel b/w gmail server and this host and to create a secure connection using TLS
    server.login('focpproject@gmail.com','room404error')
    #Logging on to the server using our credentials so that we can send gmail
    recv_emails=["umart823@gmail.com","jerry.khan7886@gmail.com","mzkhan.bscs21seecs@seecs.edu.pk"]
    for x in recv_emails:
        server.sendmail('focpproject@gmail.com',x,Messsage)
#def CityCoordinates():
    #City={"Lahore":[,],"Islamabad":[33.684422,73.047882]}
def GetWeatherData():
    lat="33.684422"
    lon="73.047882"
    api="https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=minutely,alerts,hourly,current&appid=968e39853093a073483c700d3a991167"
    #This is the URL for retrieving data
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
    if ForecastedWeather== "Rain" or "Drizzle" or "Snow" or "Thunderstorm":
        Messsage=f"Remember to take your Umbrella with you!!\nThe chance of {Description} is {int(Precipitation*100)}%"
       
    elif ForecastedWeather=="Clouds" and Precipitation>0.4:
        Messsage=f"Take your umbrella with you as it is Cloudy today and chances of rain are {int(Precipitation*100)}%"
    elif ForecastedWeather=="Clouds" and Precipitation<0.4:
        Messsage="It is Cloudy Today.Enjoy!!"
    else:
        Messsage="The weather today is Clear.Enjoy!!"
        
    
GetWeatherData()
Message()
SendMail()

    #API is a software that acts as an intermediary between 2 applications and allows one application to access services provided by the other.
    #In this case we are retrieving data on a webpage on a web server stored in JSON Format and providing it to our application using the API or Application Programming Interface

    