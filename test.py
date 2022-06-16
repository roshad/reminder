import pygetwindow as gw  
if ("OneNote" not in gw.getActiveWindowTitle()):#没有在记录
            
            # activate OneNote window
            gw.getWindowsWithTitle('OneNote')[0].activate()
            
            #不能时间到就激活,否则无意中点旁边