
from playsound import playsound
import time
import datetime
import pygetwindow as gw  
import os

startTime=None
# 10min响一次,开terminal重置,偶发无意识地重置

while True:
    try:
        #print(gw.getActiveWindowTitle())
        if ("OneNote" in gw.getActiveWindowTitle()):#在前 时间到了,在前,再重开,否则经常
            if (startTime):#正计时,停止计时
                startTime=None
                print("停止计时")
        else: #在背
            if (startTime==None): #开始计时
                startTime=datetime.datetime.now()
                print("开始计时",startTime)
            if ((datetime.datetime.now()-startTime).seconds>=600):#到10分钟,放声音,激活
                print("时间到",datetime.datetime.now().strftime('%H:%M:%S'))
                playsound("min.mp3")
                #不能时间到就激活,否则无意中点旁边
        
    except Exception as e: 
        print(e)
    time.sleep(0.1)





