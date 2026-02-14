from multiprocessing import Process
import time

def bew_chai(name):
    print(f"start of {name} chai bewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")

if __name__ == "__main__":
    chai_makers = [
        Process(target=bew_chai, args=(f"Chai maker #{i+1}",))
        for i in range(3)
    ]

    for p in chai_makers:
        p.start()
    
    for p in chai_makers:
        p.join()

    print("All chai served")
