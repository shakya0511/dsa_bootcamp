# BST -  binary search tree

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def Solution1(root):

    sums = []
    CalculateSum(root, 0, sums)

    return sums

def CalculateSum (node, runningSum, sums):

    if node is None:
        return 

    runningSum = runningSum + node.value

    if node.left is None and node.right is None:
        sums.append(runningSum)
        return 
    
    CalculateSum(node.left, runningSum, sums)
    CalculateSum(node.right, runningSum, sums)