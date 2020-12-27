
import threading 
from threading import*
import solution as x 


x.create("naaz",10,0)


x.create("raghib",730,0) 


x.read("naaz")


x.read("raghib")


x.create("sanu",5000,0)


x.modify("naaz",550)

 
x.delete("raghib")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
#as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
#as per the operation
t2.start()
t2.sleep()
