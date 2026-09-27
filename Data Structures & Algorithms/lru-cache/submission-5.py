class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.limit = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            move_node = self.cache[key]

            left = move_node.prev
            right = move_node.next
            left.next = right
            right.prev = left

            before = self.tail.prev
            before.next = move_node
            self.tail.prev = move_node
            move_node.prev = before
            move_node.next = self.tail
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value

            move_node = self.cache[key]

            left = move_node.prev
            right = move_node.next
            left.next = right
            right.prev = left

            before = self.tail.prev
            before.next = move_node
            self.tail.prev = move_node
            move_node.prev = before
            move_node.next = self.tail

        else:
            before = self.tail.prev
            new_node = ListNode(key, value, before, self.tail)
            before.next = new_node
            self.tail.prev = new_node

            if len(self.cache) == self.limit:
                result_key = self.head.next.key
                del self.cache[result_key]
                second_node = self.head.next.next
                self.head.next = second_node
                second_node.prev = self.head

            self.cache[key] = new_node

