# 节点
class Node:
    def __init__(self, value):
        self.value = value
        self.next: 'Node' = None

# 链表
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next


# 测试

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     ll.display()
#     print(ll.find(2))
#     ll.delete(2)
#     ll.display()


