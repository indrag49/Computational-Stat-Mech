## A simple application of threading in python to simulate the calculation of eta_max from algorithm number 2.8 from Werner Krauth's book
## The parallel computation in python is adapted from the book "Parallel Programming in Python", by Jan Palach  


import logging, threading
from queue import Queue
import random, math as m

def dist(k, l, Lx, Ly):
        """Calculates the distance between the two particles k and l. Lx and Ly are the lengths of the boundaries"""
        dx=abs(k[0]-l[0])%Lx
        delta_x=min(dx, Lx-dx)
        dy=abs(k[1]-l[1])%Ly
        delta_y=min(dy, Ly-dy)
        return m.sqrt(delta_x**2+delta_y**2)

def direct_disks_any(N, Lx, Ly):
        """N is the number of particles in a box of dimension Lx X Ly"""
        pairs=[]
        for i in range(N-1):
                for j in range(i+1, N): pairs+=[[i, j], ]
        pos=[(random.uniform(0, Lx), random.uniform(0, Ly)) for i in range(N)]
        sigma=min(dist(pos[i], pos[j], Lx, Ly) for i, j in pairs)/2.0
        eta_max=N*m.pi*sigma**2/(Lx*Ly)
        return eta_max


logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s - %(message)s')

ch=logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

direct_disks_any_dict={}
shared_queue=Queue()
input_list=range(2, 401)

queue_condition=threading.Condition()

def direct_disks_any_task(condition):
        with condition:
                while shared_queue.empty():
                        logger.info("[%s] - waiting for number of particles in a box of size Lx X Ly in queue.. "
                                    % threading.current_thread().name)
                        condition.wait()
                else:
                        N=shared_queue.get()
                        direct_disks_any_dict[N]=direct_disks_any(N, 5., 5.)
                shared_queue.task_done()
                logger.debug("[%s] eta_max of key [%d] with result [%f]"% (threading.current_thread().name, N, direct_disks_any_dict[N]))

def queue_task(condition):
        logging.debug('Starting queue_task...')
        with condition:
                for item in input_list:
                        shared_queue.put(item)
                logging.debug("Notifying direct_disks_any_task threads that the queue is ready to consume ...")
                condition.notifyAll()
                

threads=[threading.Thread(target=direct_disks_any_task, args=(queue_condition,)) for i in range(len(input_list))]

[thread.start() for thread in threads]

prod=threading.Thread(name='queue_task_thread', target=queue_task, args=(queue_condition,))
prod.start()

[thread.join() for thread in threads]
print(direct_disks_any_dict)