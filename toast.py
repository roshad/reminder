from win10toast import ToastNotifier

import time
index=0
#
while True:

    ToastNotifier().show_toast(
        str(index),
        threaded=True,  # 否则程序中止
        duration=0.5,  # 持续时间s,有影响
       
    )
    index+=1
    time.sleep(1)
