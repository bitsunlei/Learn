import time
import sched

schedule=sched.scheduler(time.time,time.sleep)

def func(str1,float1):
    print('Time is ',time.time,' | output=',str1,float1)

def timer(n):
    print('one minute passed')

    while True:
        print(time.strftime('%Y-%m-%d %x',time.localtime()))
        time.sleep(60)

def printHello():
    print('Hello world')

print(time.time())
# enter(delay,priority,action,arguments)
schedule.enter(2,0,func,('test1',time.time()))
schedule.enter(3,0,func,('test2',time.time()))
schedule.enter(4,0,func,('test3',time.time()))
schedule.run()
print(time.time())

for i in range(5):
    print(i)
    time.sleep(10)
