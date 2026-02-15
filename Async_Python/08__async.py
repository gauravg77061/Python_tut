import threading

chai_stock=0
def resstock():
    global chai_stock
    for _ in range(10000):
        chai_stock+=1
    
threads=[threading.Thread(target=resstock) for __ in range(2)]
for t in threads:t.start()
for t in threads:t.join()

print("chai stock: ",chai_stock)
