import cv2
import sys 
import winsound
import os
import time
import smtplib
import pyttsx3
from email.message import EmailMessage
import requests
r = requests.get('https://get.geojs.io/')
ip_request=requests.get('https://get.geojs.io/v1/ip.json')
ipAdd = ip_request.json()
import json 
from urllib.request import urlopen
url = 'https://ipinfo.io/json'
response=urlopen(url)
data=json.load(response)
url ='https://get.geojs.io/v1/ip/geo/'+data['ip']+'.json'
geo_request=requests.get(url)
geo_data = geo_request.json()
print(geo_data['longitude'])
print(geo_data['latitude'])
URL="https://www.google.com/maps/place/bennett university/@"+geo_data['longitude']+','+geo_data['latitude']
def say(text):
    engine = pyttsx3.init('sapi5')
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    engine.setProperty('rate',150)
    print("  ")
    print(f"firedetrwector: {text}")
    engine.say(text=text)
    engine.runAndWait()
    print("  ")
say("tell your email address")
q=input()
def mail():
    Address = URL
    password="jozcypwgvvvflsuv"
    msg = EmailMessage()
    msg["Subject"] = "Fire Outbreak Detected"
    msg["From"] = "yaar127308@gmail.com"
    msg["To"] = q
    msg.set_content(f"I'm FireDetectionSys,\nData:\nAddress - {Address}\nTime - {time.ctime()}")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("yaar127308@gmail.com",password )
        smtp.send_message(msg)
        smtp.close() 

def beep(duration=1000) :
            frequency = 2500  # Set Frequency To 2500 Hertz
            winsound.Beep(frequency, duration)
def shutdown():
    import time
    import sys
    time.sleep(1)
    sys.exit()
if __name__ == '__main__':
    firedetector = cv2.CascadeClassifier('C:/Users/Hp/Desktop/FDSys.xml')
    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    capture.set(3,500)
    capture.set(4,500)
    while (True):
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fire = firedetector.detectMultiScale(frame, 1.3, 5)
        for (x,y,w,h) in fire:
            cv2.destroyAllWindows()
            say("fire has been detected")
            beep()
            beep()
            beep()
            beep()
            beep()
            mail()
            say("mail has been sent to your guardian ")
            beep()
            beep()
            beep()
            beep()
            beep()
            shutdown()
        cv2.imshow('window', frame)
        if cv2.waitKey(1) == ord('q'):
            break