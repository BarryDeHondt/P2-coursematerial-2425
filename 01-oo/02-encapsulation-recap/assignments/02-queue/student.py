class Queue:
    def __init__(self):
        self.__queue = []
        
    def queue(self):
        return self.__queue
    
    
    def add(self, item):
        self.queue.append(item)
        
    def next(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        if len(self.queue) < 1:
            raise ValueError("Queue is empty")
        
        
    
        
        
        
queue = Queue()

queue.add('Alice')
queue.add('Bob')
queue.add('Charlie')

queue.next() 
        
        