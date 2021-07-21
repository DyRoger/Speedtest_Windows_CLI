import os
import time
import subprocess as sp
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
# try:
# 	os.system('cmd /k "speedtest-cli"')
# except:
# 	print("Couldn't Execute")

# For Result storing
print("starting Program")
fh = open('speedtest.txt' , 'a')
print("Collecting Result\nWaiting..........")
t_out=sp.getoutput('speedtest-cli')

fh.write('Testing Time:\t'+current_time+'\n'+t_out+'\n\n')
fh.close()

print("Result Successfully Stored")
time.sleep(3)