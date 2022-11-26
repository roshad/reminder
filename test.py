import pygetwindow as gw

for window in gw.getWindowsWithTitle('Toggl Track'):  # 最小化会有两个窗口
            # if onenote not in title
            #print(window.title)
    if (window.isMinimized):
        window.restore()
    
    window.activate() 
for window in gw.getWindowsWithTitle('Toggl Track'):  # 最小化会有两个窗口
            # if onenote not in title
            #print(window.title)
    if (window.isMinimized):
        window.restore()
    
    window.activate() 