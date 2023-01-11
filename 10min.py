
import tkinter as tk
import time
import datetime
import pygetwindow as gw
import os
from playsound import playsound
# from win10toast import ToastNotifier
# import win32gui
# import win32con
import keyboard as kb
# toaster = ToastNotifier()
# toaster.show_toast("Hello World!!!",
#                    "Python is 10 seconds awsm!",
#                    duration=10,
#                    )
sound= os.path.dirname(__file__)+'\\min.wav'

gui = tk.Tk()
tkHour = tk.IntVar()
tkLong = tk.IntVar()
# doubleV = tk.IntVar()
# hourButton = tk.Checkbutton(gui, text="60min",	variable=tkHour)
longButton = tk.Checkbutton(gui, text="加长",	variable=tkLong)
# double = tk.Checkbutton(gui, text="加长", variable=doubleV)
# hourButton.pack()
longButton.pack()
# double.pack()
# playsound("./min.wav")

def now(): return datetime.datetime.now()


lastTime = now()
def diff(): return now()-lastTime



def pinWindow():
    string = ""
    length = 4 if tkLong.get() else 2
    while True:

        time.sleep(1)

        if kb.is_pressed("esc"):
            string += 'h'
        # print(string)
        try:
            if (len(string) < length and ("Toggl Track" not in gw.getActiveWindow().title)):
                for window in gw.getWindowsWithTitle('Toggl Track'):  # 最小化会有两个窗口
                   
                    window.minimize()
                    window.restore()
            elif (len(  string) >= length):
                for window in gw.getWindowsWithTitle('Toggl Track'):  
                   
                    window.minimize()
                    window.restore()
                return

        except:
            print("error")

# pinWindow()
print(now(), "启动")


def loop():
    global lastTime, tkLong, tkHour
    # per10sec = now().second % 10 == 0
    is5 =  now().minute % 5 == 0 and now().second == 0 and tkHour.get() == 0
    is10 = now().minute % 10 == 0 and now().second == 0 
    is30 = now().minute % 30 == 0 and now().second == 0
    isHour = lastTime.hour != now().hour  # 小时不一样
    # if now().hour < 12:  # 上午加强提醒
    #     tkHour.set(0)
    #     tkLong.set(1)
    if (is30):
        print(now(), "响")
        playsound(sound)
    if (is5 or isHour):
        print(now(), "提醒", "5min" if is5 else "1hour")
        pinWindow()
    

    lastTime = now()
    time.sleep(0.1)
    gui.after(1000, loop)


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
