import webbrowser
import time

num = 0;


while (num <=2):
    print("This program began on"+time.ctime())
    webbrowser.open("https://goo.gl/")
    time.sleep(7200)
    num=num+1
