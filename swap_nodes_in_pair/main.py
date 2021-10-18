# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self, node: ListNode):
        self.head = node
        self.now = node

    def addNode(self, newNode: ListNode):
        self.now.next = newNode
        self.now = newNode

    def changeHead(self, head: ListNode):
        self.head = head

    def printList(self,head):
        self.now = head
        s = ""
        while True:
            s += str(self.now.val)
            if self.now.next is None:
                break
            self.now = self.now.next
            s += "->"

        print(s)

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        now, newhead, previous = head, head.next, None
        while True:
            # swap
            if previous:
                previous.next = now.next
            nextNode = now.next
            now.next = nextNode.next
            nextNode.next = now
            previous = now

            if not now.next or not now.next.next:
                break
            previous, now, nextNode = now, now.next, now.next.next

        return newhead 

    def swapPairRe(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swapPairRe(second.next)
        second.next = head
        return second
        


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        now, newhead, previous = head, head.next, None
        while True:
            # swap
            if previous:
                previous.next = now.next
            nextNode = now.next
            now.next = nextNode.next
            nextNode.next = now
            previous = now

            if not now.next or not now.next.next:
                break
            previous, now, nextNode = now, now.next, now.next.next

        return newhead

            

# [1,2,3,4]
arr = [1,2,3,4]
node = ListNode(arr[0])
ll = LinkList(node)
for i in range(1, len(arr)):
    newNode = ListNode(arr[i])
    ll.addNode(newNode)

ll.printList(ll.head)
# head = ll.swapPairs(ll.head)
head = ll.swapPairRe(ll.head)
ll.printList(head)
