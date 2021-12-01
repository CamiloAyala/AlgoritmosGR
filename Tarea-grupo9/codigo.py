# Python program to demonstrate searching operation
# in binary search tree without recursion
class newNode:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
        #return "{}:(i:{},d:{})".format(self.data,self.left,self.right)
 
# Function to check the given
# key exist or not
def iterativeSearch(root, key):
     
    # Traverse until root reaches
    # to dead end
    while root != None:
         
        # pass right subtree as new tree
        if key > root.data:
            root = root.right
 
        # pass left subtree as new tree
        elif key < root.data:
            root = root.left
        else:
            return True # if the key is found return 1
    return False
 
# A utility function to insert a
# new Node with given key in BST
def insert(Node, data, parent=None, dir="", tab=""):
    print(tab+"insert "+str(data),"in "+dir,parent) #depuración
    # If the tree is empty, return
    # a new Node
    if Node == None:
        Node = newNode(data)
        print(data, "inserted!\n") #depuración
        return Node
 
    # Otherwise, recur down the tree
    NodeOld = Node
    tab="\t"+tab #depuración
    if data < Node.data:
        Node.left = insert(Node.left,data, Node,"izq.",tab)
    elif data > Node.data:
        Node.right = insert(Node.right,data, Node,"der.",tab)
 
    # return the (unchanged) Node pointer
    return Node
 
# Driver Code
if __name__ == '__main__':
     
    # Let us create following BST
    #          50
    #       /      \
    #      30      70
    #     /  \    /  \
    #    20  40  60  80
    #   /
    # 10
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    insert(root, 10)
    
    if iterativeSearch(root, 15):
        print("Yes")
    else:
        print("No")
 
# This code is contributed by PranchalK