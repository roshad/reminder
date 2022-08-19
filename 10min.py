
import time
import datetime
import pygetwindow as gw
import tkinter as tk
from win10toast import ToastNotifier
# toast = ToastNotifier()

gui = tk.Tk()
c10v = tk.IntVar()
doubleV = tk.IntVar()
c10 = tk.Checkbutton(gui, text="10min",	variable=c10v)
double = tk.Checkbutton(gui, text="加长", variable=doubleV)
c10.pack()
double.pack()


def now(): return datetime.datetime.now()


lastTime = now()
def diff(): return now()-lastTime


def forwardWindow():
    time.sleep(0.1)
    try:
        if ("OneNote" not in gw.getActiveWindow().title):
            for window in gw.getWindowsWithTitle('OneNote'):  # 最小化会有两个窗口
                # if onenote not in title

                window.minimize()
                window.maximize()
    except:
        1


def loop():
    global lastTime
    # 小时不一样,停10秒

    if (lastTime.hour != now().hour):

        print(now(), "提醒", "整点")
        while (diff().seconds < (15 if doubleV.get() == 1 else 5)):
            forwardWindow()
    # 10分钟,停5秒

    if (now().minute % 10 == 0 and now().second == 0 and c10v.get() == 1):

        print(now(), "提醒", "10分钟")
        while (diff().seconds < (15 if doubleV.get() == 1 else 5)):
            forwardWindow()

    lastTime = now()
    gui.after(500, loop)


gui.after(0, loop)
gui.mainloop()


# startTime = None
# passedSec =lambda :(datetime.datetime.now()-startTime).seconds
# while True:
#     try:
#         # get current hour

#         if (startTime == None):  # 未计时
#             startTime = datetime.datetime.now()
#             print("开始计时", startTime)
#         elif (passedSec() >= 600):  # 时间到
#             print("提醒", datetime.datetime.now().strftime('%H:%M:%S'))
#             # activate OneNote window
#             # toast.show_toast(
#             #     "多离 多息",
#             #     threaded=True,  # 否则程序中止
#             #     duration=300,  # 持续时间s,有影响

#             # )
#             for window in gw.getWindowsWithTitle('OneNote'):  # 最小化会有两个窗口
#                 window.minimize()
#                 window.maximize()
#             while (passedSec()<605):
#                 print(passedSec())
#                 if (gw.getWindowsWithTitle('OneNote')!=None): #已激活好像会报错,但不影响,报错后还会进来
#                     window.activate()
#                 time.sleep(0.1)
#             startTime = None
#             #print("停止计时")
#     except Exception as e:
#         print(e)
#     time.sleep(0.1)
