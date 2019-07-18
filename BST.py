class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def is_root_empty(self):
        return self.root is None

    def find_position(self, data):
        current = self.root
        while current is not None:
            if data <= current.data:
                if current.left is None:
                    return (current, 1)
                current = current.left
            else:
                if current.right is None:
                    return (current, 2)
                current = current.right

    def add_node(self, data):
        node = self.Node(data)
        if self.is_root_empty():
            self.root = node
        else:
            current, val = self.find_position(data)
            if val == 1:
                current.left = node
            else:
                current.right = node

    def preorder(self, current):
        if current is not None:
            print (str(current.data),end = " ")
            self.preorder(current.left)
            self.preorder(current.right)

    def traverse_preorder(self):
        self.preorder(self.root)

    def inorder(self, current):
        if current is not None:
            self.inorder(current.left)
            print (str(current.data),end = " ")
            self.inorder(current.right)

    def traverse_inorder(self):
        self.inorder(self.root)

    def postorder(self, current):
        if current is not None:
            self.postorder(current.left)
            self.postorder(current.right)
            print (str(current.data),end = " ")

    def traverse_postorder(self):
        self.postorder(self.root)

    def check_leaf_node(self, node):
        return node.left is None and node.right is None
        
    def find_leaf_node(self, node):
        if node is not None:
            if self.check_leaf_node(node):
                print(node.data)
            self.find_leaf_node(node.left)
            self.find_leaf_node(node.right)

    def findAllLeafNodes(self):
        self.find_leaf_node(self.root)

def same_tree(node1, node2):
    # this has to be here to check for leaf nodes
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    return node1.data == node2.data and same_tree(node1.left, node2.left) and same_tree(node1.right, node2.right)

def size_of_binary_tree(node):
    if node is None:
        return 0
    leftSize = size_of_binary_tree(node.left)
    rightSize = size_of_binary_tree(node.right)
    return leftSize + rightSize + 1

def height(node):
    if node is None:
        return 0
    left = height(node.left)
    right = height(node.right)
    return 1 + max(left, right)

def sum_root_to_node(node, sum, listVal):
    if node is None:
        print(1)
        return False
    if node.left is None and node.right is None:
        if node.data == sum:
            listVal.append(node.data)
            return True
        else:
            return False
    if sum_root_to_node(node.left, sum - node.data, listVal):
        listVal.append(node.data)
        return True
    if sum_root_to_node(node.right, sum - node.data, listVal):
        listVal.append(node.data)
        return True
    return False


def tree_traversal_level_wise(node):
    if node is None:
        return
    level_list = []
    level_list.append(node)
    while len(level_list) == 0:
        temp = level_list.pop(0)
        print (temp.data)
        if temp.left is not None:
            level_list.append(temp.left)
        if temp.right is not None:
            level_list.append(temp.right)
        

if __name__ == "__main__":
    bst1 = BST()
    input_list = [15, 9, 20, 45, -1, 10, 17]
    for i in input_list:
        bst1.add_node(i)
    #bst.traverse_preorder()
    #print()
    bst1.traverse_inorder()
    print()
    #bst.traverse_postorder()
    #bst.findAllLeafNodes()

    #bst2 = BST()
    #input_list = [15, 9, 20, 45, -1, 10]
    #for i in input_list:
    #    bst2.add_node(i)
    #bst2.traverse_inorder()
    #print()
    #print ("are they same? :",same_tree(bst1.root, bst2.root))

    print("size: ",size_of_binary_tree(bst1.root)) 
    print("height: ",height(bst1.root))
    listVal = []
    print(sum_root_to_node(bst1.root, 23, listVal))
    print (listVal)
    print (tree_traversal_level_wise(bst1.root))
