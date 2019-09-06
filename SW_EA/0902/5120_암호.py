class Node:
    def __init__(self, data, pre=None, next=None):
        self.data = data
        self.pre = pre
        self.next = next

class LinkedList:
    def __init__(self):
        headNode = Node('head')
        self.cnt = 0
        self.tail = headNode
        self.head = headNode

    def insert(self, data):
        insertNode = Node(data)
        insertNode.pre = self.tail
        self.tail.next = insertNode
        self.tail = insertNode
        self.cnt += 1

    def find_password(self, m, k):
        current = self.head.next
        for _ in range(k):
            for _ in range(m-1):
                if current == self.tail:
                    current = self.head
                current = current.next

            if current == self.tail:
                nextNode = self.head.next
                insertNode = Node(current.data + nextNode.data)
                current.next = insertNode
                insertNode.pre = current
                self.tail = insertNode
            else:
                nextNode = current.next
                insertNode = Node(current.data + nextNode.data)
                current.next = insertNode
                insertNode.pre = current
                insertNode.next = nextNode
                nextNode.pre = insertNode
            current = insertNode
            self.cnt += 1

    def print_last_ten(self):
        current = self.tail
        for i in range(10):
            if current.data =='head': break
            print(current.data, end=' ')
            current = current.pre
        print()

for tc in range(1, int(input().strip())+1):
    n, m, k = map(int, input().strip().split())
    linked = LinkedList()
    datas = list(map(int, input().strip().split()))
    for data in datas:
        linked.insert(data)
    linked.find_password(m, k)
    print('#%d' %(tc), end=' ')
    linked.print_last_ten()
