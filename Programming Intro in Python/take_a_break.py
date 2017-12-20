import webbrowser
import time

n = 1
print ("This Program started on" + time.ctime())
while n <= 3:
    time.sleep(10)
    webbrowser.open("https://youtu.be/ACLY8BZySFs")
    n+=1

