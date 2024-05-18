from collections import deque

class MyStack:  

    def __init__(self):
        self.top_value: int
        self.queue: deque = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:

        stack_len: int = len(self.queue)

        for _ in range(stack_len-1):
            current: int = self.queue.popleft()
            self.queue.append(current)

        return self.queue.popleft()
        

    def top(self) -> int:

        stack_len: int = len(self.queue)

        if stack_len:
            for _ in range(stack_len-1):
                current: int = self.queue.popleft()
                self.queue.append(current)

            top: int = self.queue.popleft()
            self.queue.append(top)
            return top
        return

    def empty(self) -> bool:

        return not len(self.queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()