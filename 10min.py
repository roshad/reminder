
import time
import datetime
import pygetwindow as gw
import os
from win10toast_click import ToastNotifier 

startTime = datetime.datetime.now()
toast = ToastNotifier()
# 一直开着对起床以后的大段浪费效果会好点

while True:
    try:
        
        if ((datetime.datetime.now()-startTime).seconds >= 600):  # 到10分钟,放声音,激活
            print("弹窗", datetime.datetime.now().strftime('%H:%M:%S'))
            
            
            
            toast.show_toast(
                "多离 多息",
                duration=None,
                threaded=False,  # 否则程序中止
            )
            startTime=datetime.datetime.now()
            print("开始计时", startTime.strftime('%H:%M:%S'))

            
    except Exception as e:
        print(e)
    time.sleep(0.1)
