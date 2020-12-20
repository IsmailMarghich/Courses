from collections import deque

#queues using collections module
customqueue = deque(maxlen=3)

customqueue.append(1)
customqueue.append(2)
customqueue.append(3)
customqueue.append(4)
print(customqueue)
print(customqueue.popleft())
print(customqueue)
customqueue.clear()
print(customqueue)
print('------------')
#queues using queue module
import queue as q

Qqueue  = q.Queue(maxsize=3)
print(Qqueue.empty())
Qqueue.put(1)
Qqueue.put(2)
Qqueue.put(3)
print(Qqueue.full())
print(Qqueue.get())
print(Qqueue.qsize())
print('------')
from multiprocessing import Queue as m

Mqueue = m(maxsize=3)
Mqueue.put(1)
print(Mqueue.get())