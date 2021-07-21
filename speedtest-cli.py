import os
import time
import subprocess as sp
print("starting Program")
fh = open('speedtest.txt' , 'a')
# try:
# 	os.system('cmd /k "dir"')
# 	os.system('cmd /k "speedtest-cli"')
# except:
# 	print("Couldn't Execute")

# For Result storing
print("Collecting Result\nWaiting..........")
t_out=sp.getoutput('speedtest-cli')

fh.write('\n'+t_out+'\n\n')
fh.close()

print("Result Successfully Stored")
time.sleep(3)