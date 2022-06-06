
import time
import datetime
import pygetwindow as gw  


startTime=None
# 10min响一次,开terminal重置,偶发无意识地重置

while True:
    try:
        #get current hour
        
        if (startTime==None): #未计时,开始计时
            startTime=datetime.datetime.now()
            print("开始计时",startTime)
        elif ((datetime.datetime.now()-startTime).seconds>=600 ):#时间到
            if ("OneNote" not in gw.getActiveWindowTitle()):#没有在记录
                print("提醒",datetime.datetime.now().strftime('%H:%M:%S'))
                # activate OneNote window
                gw.getWindowsWithTitle('OneNote')[0].activate()
                
                #不能时间到就激活,否则无意中点旁边
            else:   
                startTime=None
                print("停止计时")
    except Exception as e: 
        print(e)
    time.sleep(0.1)





