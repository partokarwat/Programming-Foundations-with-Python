"""
For documentation of the webbrowser module,
see http://docs.python.org/library/webbrowser.html
"""
#!/usr/bin/python
import webbrowser
import time

total_breaks = 5
break_count = 0

print("Good morning! You started on " + time.ctime())
while (break_count < total_breaks):   
    time.sleep(2*60*60) # wait for 2 hours
    new = 2 # open in a new tab, if possible

    # open a public URL, in this case, the webbrowser docs
    url = "https://www.youtube.com/watch?v=izGwDsrQ1eQ"
    webbrowser.open(url,new=new)
    break_count = break_count + 1
    
print("Good bye!")


