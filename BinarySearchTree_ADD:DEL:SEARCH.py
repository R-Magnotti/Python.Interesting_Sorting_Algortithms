#######################################################################################################################
#                                          Author: Richie Magnotti
#
# Goal of code is to demonstrate both sorting AND ADDITION/DELETION/SEARCHING
#######################################################################################################################

# A utility class that represents an individual node in a BST
class Node:
    def __init__(self, value):
        self.leftChild = None
        self.rightChild = None
        self.data = value

# root = root node and key = key searching for
def delete(root, key):
    if root is None:
        print("This node could not be located. Try another value.")
        return root

    if key < root.data:
        delete(root.leftChild, key)

    elif key > root.data:
        delete(root.rightChild, key)

    else:
        #if the root has no children
        if root.rightChild is None and root.leftChild is None:
            print("no children nodes.")
            root = None

        #if the root has 1 child
        elif (root.leftChild is None) and (root.rightChild is not None):
            print(root.data, " has only 1 right child node")
            temp = root.rightChild.data
            root.rightChild = None
            root.data = temp

        elif (root.rightChild is None) and (root.leftChild is not None):
            print(root.data, " has only 1 left child node")
            temp = root.leftChild.data
            root.leftChild = None
            root.data = temp

            #if the root has 2 children
            #elif (root.rightChild is not None) and (root.leftChild is not None):
            print(root.data, " has two child nodes")
            min = findMin(root.rightChild)
            temp = min.data
            min = None
            root.data = temp

#root = root node and s = key searching for
def search(root, key):
    if root is None:
        print("This node could not be located. Try another value.")
        return root

    if key < root.data:
        search(root.leftChild, key)

    elif key>root.data:
        search(root.rightChild,key)

    else:
        print("root value = key value ", root.data, " = ", key, "The node belonging to this key value has been found.")

def findMax(root):
    if root.rightChild:
        findMax(root.rightChild)
    else:
        print("the max value is: ", root.data)
        return root

def findMin(root):
    if root.leftChild:
        findMin(root.leftChild)
    else:
        print("the min value is: ", root.data)
        return root

    # recursive function to make a node equal to each value in the initial list
def insert(root, node):
    #if root is empty set it equal to the passed value
    if root is None:
        root = node
    else:
        # if the new data is less than the root data and the node has no left child
        # then make the node's left child node reference the current node
        if root.data > node.data:
            if root.leftChild is None:
                root.leftChild = node
            else:
                # if the new data is less than the root data and the node does have a left child
                # then recursively call back the insert function but pass the root's left child and
                # run through the tests again
                insert(root.leftChild, node)
        else:
            if root.rightChild is None:
                root.rightChild = node
            else:
                insert(root.rightChild, node)

def inorder(root):
    if root:
        inorder(root.leftChild)
        list
        print(root.data)
        inorder(root.rightChild)

def main():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = Node(A[0])
    i = 0
    #for all items, to insert, pass the root node and the new node to be added
    #needed to modify the range to avoid two identical root nodes because when the root node
    #is created it accepts the initial value of the list
    for item in range(i+1, len(A)):
        insert(n, Node(A[item]))
        i = i+1

    findMax(n)
    findMin(n)
    print("\n")

    print("Searching for node key value of ", 5)
    search(n,5)
    print("\n")

    print("The tree before deleting this node: ")
    inorder(n)
    delete(n,9)
    print("The tree after deleting this node: ")
    inorder(n)


if __name__ == "__main__":
    main()