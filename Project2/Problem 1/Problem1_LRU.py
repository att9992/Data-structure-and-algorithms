class Node(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    def __str__(self):
        return "(%s,%s)" % (self.key,self.value)

class LRU_Cache(object):
    def __init__(self,capacity):
        self.head = None
        self.end = None
        self.hash = {}
        self.capacity = capacity 
        self.size = 0

    def set_head(self,node):
        if not self.head:
            self.head = node
            self.end = node
        else:
            node.prev = None
            node.next = self.head
            self.head.prev=node
            self.head = node
        self.size += 1

    def remove(self,node):
        if not self.head:
            return
        
        if self.head == node and self.end == node:
            self.head = None
            self.end = None

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        if self.end == node:
            self.end = self.end.prev
            self.end.next = None
        self.size -= 1
        return node


    def get(self,key):
        if key not in self.hash:
            return -1
        node = self.hash[key]
        if self.head == None:
            return node.value
        self.remove(node)
        self.set_head(node)
        return node.value
    
    def put(self,key,value):
        if key in self.hash:
            node = self.hash[key]
            if self.head != node:
                self.remove(node)
                self.set_head(node)
        new_node = Node (key,value)
        if self.size == self.capacity:
            del self.hash[self.end.key]
            self.remove(self.end)
        self.set_head(new_node)
        self.hash[key]=new_node

    def print_elements(self):
        n = self.head
        print("[head = %s, end = %s]" % (self.head, self.end), end=" ")
        while n:
            print("%s -> " % (n), end = "")
            n = n.next
        print("NULL")
        
our_cache = LRU_Cache(5)

our_cache.put(1, 1)
our_cache.put(2, 2)
our_cache.put(3, 3)
our_cache.put(4, 4)

our_cache.get(1)       
our_cache.get(2)       
our_cache.get(9)      

our_cache.put(5, 5) 
our_cache.put(6, 6)

our_cache.get(3) 
our_cache.print_elements()

our_cache = LRU_Cache(2)
our_cache.put(1, 1)
our_cache.put(2, 2)
our_cache.put(1, 10)
print(our_cache.get(1))
print(our_cache.get(2))


