import datetime
from playsound import playsound
alarmhour= int(input("enter hour:"))
alarmMin = int (input("enter Minute:"))
alarmAmPm = input("Am/Pm  :")
if alarmAmPm =="Pm":
    alarmhour+=12
while True:
    if alarmhour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("----playing----")
        playsound("orange.mp3")
        break
