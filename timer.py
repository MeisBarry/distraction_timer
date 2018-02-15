import os
import time
import sys

def min_timer(mins,beeps=2,freq=3000):
    start = time.time()
    now = time.time()
    print("\rStarting {} min session...".format(mins))
    while start+(mins*60) > now:
        now = time.time()
        sys.stdout.write("\r{}".format(time.strftime("%M:%S",time.gmtime(start+mins*60-now))))
        sys.stdout.flush()
        time.sleep(0.2)
    for i in range(beeps):
        os.system("play --no-show-progress --null --channels 1\
                   synth 0.1 sine {} vol 0.3".format(freq))
        time.sleep(0.1)

while True:
    min_timer(12)
    min_timer(3,beeps=3,freq=1000)
            



