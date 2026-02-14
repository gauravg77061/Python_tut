import threading 
import time 

def boil_milk():
    print(f"Boiling milk...")
    time.sleep(2)
    print(f"Milk boiled")

def toast_bun():
    print(f"toasting bun...")
    time.sleep(3)
    print(f"Done with bun toast")

#In this ek hi thread par dono run kar rahe 
# boil_milk()
# toast_bun()
# ham do thread create kar sakte h 
start=time.time()
t1=threading.Thread(target=boil_milk)
t2=threading.Thread(target=toast_bun)
t1.start()
t2.start()
t1.join()
t2.join()

end=time.time()

print(f"Breakfast read in {end-start} sec")