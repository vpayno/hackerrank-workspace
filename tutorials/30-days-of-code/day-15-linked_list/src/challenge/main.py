class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def display(self, head):
        current = head
        while current:
            current = current.next

    def insert(self, head, data):
        if head is None:
            head = Node(data)
        else:
            last = None
            current = head
            while current:
                last = current
                current = current.next
            if last:
                last.next = Node(data)

        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
