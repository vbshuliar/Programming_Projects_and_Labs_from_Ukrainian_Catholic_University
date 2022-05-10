"""Converts stack to queue or queue to stack."""

from arraystack import ArrayStack
from arrayqueue import ArrayQueue


def queue_to_stack(data):
    """Stack to queue."""
    temp = ArrayQueue()
    new = ArrayStack()
    for _ in data:
        temp.add(_)
    for _ in range(len(temp)):
        new.push(temp.peek())
        temp.pop()
    return new


if __name__ == "__main__":
    queue = ArrayQueue([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    stack = queue_to_stack(queue)
    print(queue)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(stack)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(stack.pop())
    # 0
    print(queue.pop())
    # 0
    stack.add(11)
    queue.add(11)
    print(queue)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    print(stack)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
