class ListNode:

    def __init__(self, value: str):
        self.value: str = value
        self.next: ListNode = None
        self.prev: ListNode = None

class BrowserHistory:

    def __init__(self, homepage: str):

        self.current: ListNode = ListNode(homepage)

    def visit(self, url: str) -> None:

        new: ListNode = ListNode(url)
        new.prev = self.current
        self.current.next = new
        self.current = self.current.next
        

    def back(self, steps: int) -> str:
        
        count: int = 0

        while self.current.prev and count < steps:
            self.current = self.current.prev
            count += 1

        return self.current.value

    def forward(self, steps: int) -> str:

        count: int = 0

        while self.current.next and count < steps:
            self.current = self.current.next
            count += 1
        
        return self.current.value


# Your BrowserHistory object will be instantiated and called as such:
obj: BrowserHistory = BrowserHistory("leetcode.com")
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")

print(obj.back(1))

# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)