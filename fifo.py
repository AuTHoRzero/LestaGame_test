from queue import SimpleQueue
from collections import deque

class Fifo(SimpleQueue):

    '''
    Данный класс представляет собой очередь FIFO, в отличии от приведённого ниже,
    тут используется класс deque, позволяющий более быстро вставлять и удалять элем-ты,
    благодаря родительскому классу, использует multiprocessing, что позволяет работать
    с объектами очереди параллельно.
    '''

    def __iter__(self):
        return self
    
    def __len__(self):
        return self.qsize()
    
    def __next__(self):
        if not self.empty():
            return self.get()
        raise StopIteration
    
    def enqueue(self, item):
        return super().put(item)
    
    def dequeue(self):
        return super().get()
    
    def isEmpty(self):
        return super().empty()


class FifoSecond():
    '''
    Данный класс представляет собой простую очередь FIFO, в отличии от первого,
    данный класс более медленный, за счёт того, что при удалении или вставке элемента
    происходит сдвиг всех остальных.
    '''
    def __init__(self):
        self.queue = []

    def append(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        raise StopIteration


class FifoHand():
    '''
    Аналог первого варианта, без multiprocessing.
    '''
    def __init__(self) -> None:
        self.queue = deque()

    def enque(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.popleft()

    def __iter__(self):
        return  self
    
    def isEmpty(self):
        return len(self.queue) == 0
    def __next__(self):
        if not self.isEmpty():
            return self.queue.popleft()
        raise StopIteration

    
