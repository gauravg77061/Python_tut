from multiprocessing import Process
import time

def crunch_number():
    print(f"started count proces...")
    count=0
    for _ in range(100000000):
        count+=1
    print(f"Ended the count process...")


# you can also write loop but we will
#manulally create 2 process

if __name__=="__main__":
    start=time.time()
    p1=Process(target=crunch_number)
    p2=Process(target=crunch_number)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end=time.time()
    print(f"total time calculated {end-start} sec")
   