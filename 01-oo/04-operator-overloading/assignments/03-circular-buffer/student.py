class CircularBuffer:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []
        
    def __len__(self):
        return len(self.list)
    
    def add(self, item):
        if len(self.list) < self.max_size:
            self.list.append(item)
        else:
            self.list.pop(0)
            self.list.append(item)
            
    def __getitem__(self, index):
        return self.list[index]
            
    
    
        
buffer = CircularBuffer(3)

buffer.add('a')
buffer.add('b')
buffer.add('c')
buffer.add('d')

print(len(buffer))
print(buffer[0])
print(buffer[1])
print(buffer[2])
        