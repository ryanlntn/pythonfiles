#
# Linked_lists.py
#
class LinkedList:
    def __init__(self):
        self.length = 0
        self.head   = None

    def print_backward(self):
        print "[",
        if self.head != None:
            self.head.print_backward()
        print "]",

    def addFirst(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length + 1

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

    def print_list(node):
        print "[",
        while node:
            print node,",",
            node = node.next
        print "]"

    def print_backward(list):
        if list == None: return
        head = list
        tail = list.next
        print_backward(tail)
        print head,

    def removeSecond(list):
        if list == None: return
        first = list
        second = list.next
        # make the first node refer to the third
        first.next = second.next
        # separate the second node from the rest of the list
        second.next = None
        return second

    
