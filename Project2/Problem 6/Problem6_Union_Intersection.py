class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
    def to_list(self):
        output = []
        node = self.head
        while node:
            output.append(node.value)
            node = node.next
        return output

def union(llist_1, llist_2):
    list1=llist_1.to_list()
    list2=llist_2.to_list()
    output = list(set(list1+list2))
    link_list = LinkedList()
    for i in output:
        link_list.append(i)
    return link_list

def intersection(llist_1, llist_2):
    list1=llist_1.to_list()
    list2=llist_2.to_list()
    output = [i for i in list1 if i not in list2]
    link_list = LinkedList()
    for i in output:
        link_list.append(i)
    return link_list

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))