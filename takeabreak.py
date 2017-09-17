import webbrowser
import time
total_breaks = 3
count = 0
while (count < total_breaks) :
    count +=1
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=oNWOC_Pvo4w")
    print 'Time to break'
    print count
