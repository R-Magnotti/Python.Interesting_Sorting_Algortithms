#######################################################################################################################
#                                          Author: Richie Magnotti
#
# Goal of code is to demonstrate sorting via binary search tree
#######################################################################################################################

# A utility class that represents an individual node in a BST
class Node:
    def __init__(self, value):
        self.leftChild = None
        self.rightChild = None
        self.data = value

def search(data, node, parent=None):
    if data < node.data:
        if node.leftChild is None:
            return None, None
        return search(data, node)
    elif data > node.data:
        if node.rightChild is None:
            return None, None
        return search(data, node)
    else:
        return node, parent

    # recursive function to make a node equal to each value in the initial list
def insert(rootVal, node):
    if rootVal is None:
        rootVal = node
    else:
        if rootVal.data > node.data:
            if rootVal.leftChild == None:
                rootVal.leftChild = node
            else:
                insert(rootVal.leftChild, node)
        else:
            if rootVal.rightChild == None:
                rootVal.rightChild = node
            else:
                insert(rootVal.rightChild, node)


def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.leftChild)

        # then print the data of node
        print(root.data),

        # now recur on right child
        printInorder(root.rightChild)

def findMax(root):
    if not root:
        return
    findMax(root.rightChild)


def main():
    A = [5,4,6,8,2,1,7]
    root = Node(A[0])
    for item in A:
        insert(root, Node(item))

    print("Print by traversing by in-order: ")
    printInorder(root)

    # search(11,root)
    # print(search())


if __name__ == "__main__":
    main()