
import time
import datetime
import pygetwindow as gw
from win10toast import ToastNotifier
toast = ToastNotifier()
startTime = None
while True:
    try:
        # get current hour

        if (startTime == None):  # 未计时,开始计时
            startTime = datetime.datetime.now()
            print("开始计时", startTime)
        elif ((datetime.datetime.now()-startTime).seconds >= 600):  # 时间到
            print("提醒", datetime.datetime.now().strftime('%H:%M:%S'))
            # activate OneNote window
            for window in gw.getWindowsWithTitle('OneNote'):  # 最小化会有两个窗口
                toast.show_toast(
                    "多离 多息",
                    threaded=True,  # 否则程序中止
                )
                window.minimize()
                window.maximize()


            startTime = None
            print("停止计时")
    except Exception as e:
        print(e)
    time.sleep(0.1)
