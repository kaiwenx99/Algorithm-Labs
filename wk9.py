class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

def bfs_badqueue(root):
    if not root:
        return []

    queue = Queue()
    queue.enqueue(root)
    result = []

    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.value)
        for child in node.children:
            queue.enqueue(child)

    return result
