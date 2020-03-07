import sys

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

def timeToDrink(times, numOfTaps):
    dummy = Node(None)
    cur = dummy
    for t in times:
        node = Node(t)
        cur.next = node
        cur = cur.next
    i = 1
    while dummy.next:
        prev = dummy
        cur = prev.next
        for _ in range(numOfTaps):
            if not cur:
                break
            cur.val -= 1
            if not cur.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        i += 1
    return i


if __name__ == "__main__":
    f = open("7.out", 'r')
    queueSize, numOfTaps = map(int, f.readline().strip().split())
    times = map(int, f.readline().strip().split())
    f.close()
    print(timeToDrink(times, numOfTaps))
