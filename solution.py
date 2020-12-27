import threading 
#this is for python 3.0 and above. use import thread for python2.0 versions
from threading import*
import time

d={} #d is dictionary for key value pair store....

#for create operation

def create(key,value,timeout=0):
    if key in d:
        print("Error:key already exist in store")
    else:
        if key.isalpha():
            if len(d)<(1024**3) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:
                    d[key]=l
                else:
                    print("Error:memory size exceeded")
        else:
            print("Error:Invalid key,key should contain alphabets")

#for read operation......

def read(key):
    if key not in d:
        print("Error :given key does not exist")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                str1=str(key)+":"+str(b[0])
                return str1
            else:
                print("Error",key,"Has expired")
        else:
            str1=str(key)+":"+str(b[0])
            return str1
#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in d:
        print("error: given key does not exist in Store") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("Error:",key,"has expired") #error message5
        else:
            del d[key]
            print("key is successfully deleted")


#for modify operation 


def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("Error: given key does not exist in Store") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("Error:",key,"has expired") #error message5
    else:
        if key not in d:
            print("Error: given key does not exist in Store.") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
