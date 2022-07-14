# Problem 1 - Moving Average from Data Stream
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size): Initializes the object with the size of the window size.
# double next(int val): Returns the moving average of the last size values of the stream.
# Examples

# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

from collections import deque
import queue


class MovingAverage:
    def __init__(self, size: int):
        self.sum = 0
        self.size = size
        self.queue = deque()

    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.queue.append(val)
            self.sum += val
            return self.sum / len(self.queue)
        else:
            self.queue.append(val)
            eliminated = self.queue.popleft()
            self.sum = self.sum - eliminated + val
            return self.sum / self.size


size = 3
obj = MovingAverage(size)
# assert obj.next(1) == 1   # [1]
# print(obj.next(1))
# assert obj.next(11) == 6  # [1 11]
# assert obj.next(3) == 5   # [1 11 3]
# 1. add 4 to queue
# 2. remove 1 from queue
# assert obj.next(4) == 6  # 1 [11 3 4]
# 1. adding 8 to queue
# 2. removing 11 from queue
# assert obj.next(8) == 5   # 1 11 [3 4 8]
print(obj.next(1))
print(obj.next(11))
print(obj.next(3))
print(obj.next(4))
print(obj.next(8))
