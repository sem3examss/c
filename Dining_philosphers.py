import threading
import random
import time

class Philosopher(threading.Thread):
    running = True   

    def _init_(self, index, forkOnLeft, forkOnRight):
        threading.Thread._init_(self)
        self.index = index
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight
           
    def run(self):
        while self.running: #true
            time.sleep(random.uniform(2, 5))
            print('Philosopher %s => hungry.' % self.index)
            self.dine() 

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
        while self.running:
            fork1.acquire()
            is_free = fork2.acquire(False)
            if is_free: break 
            fork1.release()
            
            print('Philosopher %s => swaps forks.' % self.index)
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining()
        fork2.release()
        fork1.release()
    def dining(self):
        print('Philosopher %s => eating. ' % self.index)
        time.sleep(random.uniform(1, 5))
        print('Philosopher %s => finishes eating => thinking.' % self.index)
forks = [threading.Semaphore() for n in range(5)]  
philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]
Philosopher.running = True 
for p in philosophers:
    p.start()
time.sleep(10)
Philosopher.running = False
print("done")