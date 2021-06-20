class Node:
    def __init__(self,x=None,next_node=None):
        self.data = x
        self.next_node = next_node 


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_ll(self):
        l = ""
        node = self.head
        if node is None:
            print("Empty")
            return 12
        while node :
            l += str(node.data) + "-> "
            node = node.next_node
        print(l)

    def insert_beginning(self,data):
        node = Node(data,self.head)
        
        if self.head is None:
            #self.head = node
            self.tail = node
        
        self.head =node 
    
    def insert_end(self,data):
        if self.head is None:
            self.insert_beginning(data)
            return
       
        node = Node(data,None)
        self.tail.next_node = node
        self.tail = node

    def to_list(self):
        a = []
        node = self.head
        while node:
            a.append(node.data)
            node = node.next_node
        return a

    def get_data_by_id(self,user_id):
        node = self.head
        while node:
            if node.data["id"] == int(user_id):
                return node.data
            node = node.next_node
        return 0

