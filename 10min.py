
import time
import datetime
import pygetwindow as gw  


startTime=datetime.datetime.now()
# 10min响一次,开terminal重置,偶发无意识地重置

while True:
    try:
        #get current hour
        
       
        if ((datetime.datetime.now()-startTime).seconds%300==0 ):#时间到           
            if ("Track" not in gw.getActiveWindowTitle()):
                print("提醒",datetime.datetime.now().strftime('%H:%M:%S'))
                # activate OneNote window
                gw.getWindowsWithTitle('Toggl')[0].minimize()
                gw.getWindowsWithTitle('Toggl')[0].maximize()
                gw.getWindowsWithTitle('Toggl')[0].activate()
                #不能时间到就激活,否则无意中点旁边
        
    except Exception as e: 
        print(e)
    time.sleep(0.5)





