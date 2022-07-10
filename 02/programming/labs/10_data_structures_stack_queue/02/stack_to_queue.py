"""Converts stack to queue or queue to stack."""

from arraystack import ArrayStack
from arrayqueue import ArrayQueue


def stack_to_queue(data):
    """Stack to queue."""
    temp = ArrayStack()
    new = ArrayQueue()
    for _ in data:
        temp.add(_)
    for _ in range(len(temp)):
        new.add(temp.peek())
        temp.pop()
    return new


if __name__ == "__main__":
    stack = ArrayStack()
    for i in range(10):
        stack.add(i)
    queue = stack_to_queue(stack)
    print(queue)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(stack)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(stack.pop())
    # 9
    print(queue.pop())
    # 9
    stack.add(11)
    queue.add(11)
    print(queue)
    # [8, 7, 6, 5, 4, 3, 2, 1, 0, 11]
    print(stack)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 11]
