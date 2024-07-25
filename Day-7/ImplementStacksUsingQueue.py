from collections import deque
class MyStack:
    def __init__(self):
        self.deque = deque()
    
    def push(self, x:int)->None:
        size = len(self.queue)
        self.queue.append(x)
        for _ in range(size):
            self.queue.append(self.queue.popleft())
    
    def pop(self)->int:
        return self.queue.popleft()
    
    def top(self)->int:
        return self.queue[0]
    
    def empty(self)->bool:
        return not self.queue
    
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())   
print(myStack.pop())   
print(myStack.empty())

