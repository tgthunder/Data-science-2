# Important concept-->Time
# Popular Modules--> 1.time(library) 2.datetime(python-class)

from time import *
from datetime import *

# epoch --> In the context of time it is the point at which time starts

passed_seconds = time() # passed time in sec since current year starts

print(passed_seconds)

# Getting current date details

print("-----------------------")
tdm = datetime.now()
print("Total time: {0}\nDate: {1}\nYear: {2}\nTime: {3}".format(tdm , tdm.date(),tdm.year ,tdm.time()))

current_details = ctime() # string which return all the details 
print(current_details)

# Finding the execution time of a programm

t1 = perf_counter()

# Do some processing

i , sum = 0 ,0

while(i<10000):
    sum+=i
    i+=1

print(sum)

t2=perf_counter()

sleep(3) # processor off for 3 sec still perf_counter will count the time

print("Execution time: {} seconds".format(t2-t1))

