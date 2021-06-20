class Node:
    def __init__(self,x=None,next_node=None):
        self.data = x
        self.next_node = next_node 

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        if self.head is None:
            print("Queue is Empty in dequeue")
            return

        #print("Popped Value :", self.head.data)
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
            return data
        
        

        self.head = self.head.next_node
        return data
        

    def print_q(self):
        if self.head is None:
            print("Queue Empty")
            return

        node = self.head
        l = ""
        while node:
            l += str(node.data)+" -> "
            node = node.next_node
        
        l+="None"
        print(l)

"""
q = Queue()
q.enqueue(10)
q.enqueue(90)
q.enqueue(101)
q.print_q()
q.dequeue()
q.print_q()
q.dequeue()
q.print_q()
q.dequeue()
q.print_q()
q.enqueue(100)
q.print_q()
q.dequeue()
q.print_q()
"""