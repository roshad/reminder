from win10toast import ToastNotifier
toast = ToastNotifier()
toast.show_toast(
    "Notification",
    "Notification body",
    duration = 10,
   
    threaded = True,
)