# 双向链表实现

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" <-> ")
            cur = cur.next
        print("None")

# 示例用法
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.display()  # 输出: 1 <-> 2 <-> 3 <-> None