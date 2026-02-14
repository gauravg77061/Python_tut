import threading
import time

def prepare_chai(type_,wait_time):
    print(f"{type_} chai brewing...")
    time.sleep(wait_time)
    print(f"{type_} chail ready ")

start=time.time()

t1=threading.Thread(target=prepare_chai,args=('Masala',2))
t2=threading.Thread(target=prepare_chai,args=('Ginger',3))

t1.start()
t2.start()
t1.join()
t2.join()

end=time.time()
print(f"total time{end-start}")
