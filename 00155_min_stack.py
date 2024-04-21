from typing import List

class Node:

    def __init__(self, value):
        self.value: int = value
        self.min: int



class MinStack:

    def __init__(self):

        self.min_stack: list[Node] = []

        # I could implement with two stacks (lists) here instead of making my own data-structure to hold two values.
        

    def push(self, val: int) -> None:

        new_node: Node = Node(val)


        if len(self.min_stack) == 0:
            new_node.min = val
        elif self.min_stack[-1].min > val:
            new_node.min = val
        else:
            new_node.min = self.min_stack[-1].min

        # Could use the min function above here to clean up this logic a little.

        self.min_stack.append(new_node)
        

    def pop(self) -> None:
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.min_stack[-1].value
        

    def getMin(self) -> int:
        return self.min_stack[-1].min
    