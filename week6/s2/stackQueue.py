# Problem 2 - Queue using Stacks
# We are given a stack data structure that supports standard operations like (push, pop, peek, and empty), implement a queue using instances of stack data structure and operations on them.

# Implement a Queue class with the following methods:

# void push(int x): Pushes element x to the back of the queue.
# int pop(): Removes the element from the front of the queue and returns it.
# int peek(): Returns the element at the front of the queue.
# boolean empty(): Returns true if the queue is empty, false otherwise.
# Example:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, x: int):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        if self._stack:
            return self._stack[-1]
        return None

    def empty(self):
        return len(self._stack) == 0

    def __len__(self):
        return len(self._stack)


class stackQueue:
    def __init__(self):
        self._stack_push = Stack()
        self._stack_pop = Stack()

    def push(self, x: int):
        while len(self._stack_push) != 0:
            self._stack_pop.push(self._stack_push.pop())

        self._stack_push.push(x)

        while len(self._stack_pop) != 0:
            self._stack_push.push(self._stack_pop.pop())

    def pop(self) -> int:
        return self._stack_push.pop()

    def peek(self) -> int:
        return self._stack_push.peek()

    def empty(self) -> bool:
        if len(self._stack_push) == 0:
            return True
        else:
            return False


sq = stackQueue()
sq.push(1)
sq.push(2)
print(sq.peek())
print(sq.pop())
