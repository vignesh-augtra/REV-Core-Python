import time
import datetime

def show_time():
    current_time = datetime.datetime.now()
    print(" {}:{}:{} ".format(current_time.hour, current_time.minute, current_time.second))

while(True):
    show_time()
    time.sleep(1)
