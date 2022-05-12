
from playsound import playsound
import time
import datetime
import pygetwindow as gw  
import os

lastTime=datetime.datetime.now()
# 10min响一次,开terminal重置,偶发无意识地重置
a= os.path.dirname(__file__)+'\\min.wav'
playsound(a)
while True:
    try:
       
        if (datetime.datetime.now().hour!=lastTime.hour):
            playsound(a) 
            playsound(a)
            lastTime=datetime.datetime.now()
            print("1小时")
        elif ((datetime.datetime.now().minute-lastTime.minute)>=10 ):#时间到
          
            playsound(a)
            #不能时间到就激活,否则无意中点旁边
            lastTime=datetime.datetime.now()
            print("10分钟")
    except Exception as e: 
        print(e)
    time.sleep(1)





