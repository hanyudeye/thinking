# 循环链表实现

class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # 指向自己
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = new_node
        new_node.next = self.head

    def display(self, count=10):
        cur = self.head
        n = 0
        if not cur:
            print("Empty list")
            return
        while n < count:
            print(cur.data, end=" -> ")
            cur = cur.next
            n += 1
            if cur == self.head:
                break
        print("(循环到头)")

# 示例用法
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.display()  # 输出: 1 -> 2 -> 3 -> (循环到头)