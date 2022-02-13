import tkinter as gui
import requests
# A module that allows sending http requests. We will use it to make the API Call.
#import time
#A module that allows us to manipulate time and in our case convert time given in Seconds sinche epoch to Local Time
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
        emaillist.pop[-1]
def filewrite():
    file=open('emaillist.txt','a')
    x=" "+ EmailEntry.get()
    NewEntry=EmailEntry.get()
    file.write(x)
    EmailEntry.delete(0,len(EmailEntry.get()))
    server.sendmail('focpproject@gmail.com',NewEntry,'Thank You for Subscribing to Our Service')
    server.quit()
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
    
#def CityCoordinates():
    #City={"Lahore":[,],"Islamabad":[33.684422,73.047882]}
def GetWeatherDataDaily():
    lat="33.684422"
    lon="73.047882"
    #Coordinates={'Lahore':[,]}
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
def GetWeatherDataCurrent():
    global Temperature
    global FeelsLike
    global Wind
    global Description
    Temperature=int(json_WeatherData["current"]["temp"]-273.15)
    FeelsLike=int(json_WeatherData["current"]["feels_like"]-273.15)
    Wind=round(json_WeatherData["current"]["wind_speed"]*3.6,2)
    Description=json_WeatherData["current"]["weather"][0]["description"].upper()
    
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
GetWeatherDataCurrent()
Message()
fileread()
SendMail()

# GUI START
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

WeatherCanvas.create_text(310,180,text=str(Temperature)+"°C",font=WeatherFont3,fill="White")
#logo of weather
logo1=gui.PhotoImage(file="icon3.png")
WeatherCanvas.create_image(100,225,image=logo1)
#Line 
WeatherCanvas.create_text(192,225,text="|",font=('Times New Roman',180),fill='White')
#Displaying descryption"
if ForecastedWeather=='Clear':
    WeatherCanvas.create_text(315,280,text='Clear Sky',font=WeatherFont2,fill="Black")
    WeatherCanvas.create_text(380,330,text="WindSpeed: "+str(Wind)+" kph  |"+"  Feels like "+str(FeelsLike)+"°C",font=8)
    logo1=gui.PhotoImage(file="icon1.png")
    WeatherCanvas.create_image(92,235,image=logo1)
if ForecastedWeather=='Clouds':
    WeatherCanvas.create_text(297,280,text='Cloudy',font=WeatherFont2,fill="Black")
    WeatherCanvas.create_text(380,330,text="WindSpeed: "+str(Wind)+" kph  |"+"  Feels like "+str(FeelsLike)+"°C",font=8)
    logo1=gui.PhotoImage(file="icon2.png")
    WeatherCanvas.create_image(100,225,image=logo1)
if ForecastedWeather in ['Rain','Drizzle','Thunderstorm']:
    WeatherCanvas.create_text(285,280,text='Rainy',font=WeatherFont2,fill="Black")
    WeatherCanvas.create_text(380,330,text="WindSpeed: "+str(Wind)+" kph  |"+"  Feels like "+str(FeelsLike)+"°C",font=8)
    logo1=gui.PhotoImage(file="icon3.png")
    WeatherCanvas.create_image(95,245,image=logo1)
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
window.mainloop()
              #API is a software that acts as an intermediary between 2 applications and allows one application to access services provided by the other.
              #In this case we are retrieving data on a webpage on a web server stored in JSON Format and providing it to our application using the API or Application Programming Interface
