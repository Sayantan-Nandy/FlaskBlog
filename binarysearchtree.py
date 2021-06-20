class Node:
    def __init__(self,data=None):
        self.data = data
        self.right_node = None
        self.left_node = None

class binarysearchtree:
    def __init__(self) -> None:
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        
        else:
            self._insert_node(data,self.root)

    def _insert_node(self,value,node):
        if node:
            if value["id"] > node.data["id"]:
                if node.right_node is None:
                    node.right_node = Node(value)
                else:
                    self._insert_node(value,node.right_node)
            else:
                if node.left_node is None:
                    node.left_node = Node(value)
                else:
                    self._insert_node(value,node.left_node)
        return
                

    def search_node(self,value):
        if self.root is None:
            return False
        
        else:
            return self._search_node_recursive(value,self.root)
    
    def _search_node_recursive(self,value,node):
        if node:
            #print(node.data["id"])
            if node.data["id"] == value:
                print("Value present")
                return node.data
            elif node.data["id"] > value:
                return self._search_node_recursive(value,node.left_node)
            elif node.data["id"] < value:
                return self._search_node_recursive(value,node.right_node)
        else:
            print("Not in Tree")
            return False

    def print_tree_wrap(self):
        if self.root is None:
            print("Tree Empty")
            return
        else:
            self._print_tree(self.root)

    def _print_tree(self,node):
        if node:
            self._print_tree(node.left_node)
            print(node.data)
            self._print_tree(node.right_node)         
        #return
    