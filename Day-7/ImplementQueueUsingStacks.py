class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def push(self ,x:int)->None:
        self.stack_in.append(x)
    
    def pop(self)->int:
        self.move_in_to_out()
        return self.stack_out.pop()
    
    def peek(self)->int:
        self.move_in_to_out()
        return self.stack_out[-1]
    
    def empty(self)->bool:
        return not self.stack_in and not self.stack_out
    
    def move_in_to_out(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())

