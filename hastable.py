class Node:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

class Data:
    def __init__(self,key=None,value=None):
        self.value=value
        self.key=key

class HashTable:
    def __init__(self,tab_size=None):
        self.table_size= tab_size
        self.hashtable = [None] * self.table_size
        
    def create_hash(self,key):
        hash_val = 0
        for i in key:
            hash_val = ord(i)
            hash_val = (hash_val*ord(i)) % self.table_size
        return hash_val
    
    def add_key(self,key,value):
        hash_val = self.create_hash(key)
        if self.hashtable[hash_val] == None:
            print("here",hash_val)
            self.hashtable[hash_val] = Node(Data(key,value),None)
        
        else:
            node = self.hashtable[hash_val]
            while node.next_node:
                node = node.next_node
            node.next_node = Node(Data(key,value),None)

    def get_val(self,key):
        hash_val = self.create_hash(key)
        if self.hashtable[hash_val] == None:
            return None
        else :
            node = self.hashtable[hash_val]
            if node.next_node is None:
                return node.data.value
            else:
                while node:
                    if(node.data.key == key):
                        return node.data.value    
                    node = node.next_node
    def print_table(self):
        print("{")
        for i, val in enumerate(self.hashtable):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        llist_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> "
                        )
                        node = node.next_node
                    llist_string += (
                        str(node.data.key) + " : " + str(node.data.value) + " --> None"
                    )
                    print(f"    [{i}] {llist_string}")
                else:
                    print(f"    [{i}] {val.data.key} : {val.data.value}")
            else:
                print(f"    [{i}] {val}")
        print("}")

        
    



        