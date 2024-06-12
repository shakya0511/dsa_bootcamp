# class is already given for a tree
# we have to find out closest number to given target 
# first thing needed is difference -> target - number, minimum number is the answer
# binary tree have few property by which for a node if value lie left to node means it is smaller and if right them bigger than node
#  

def findClosestValueInBst(tree, target):
    return InternalFunction(tree, target, tree.value)


def InternalFunction(tree, target, closest_val):

    if tree is None:
        return closest_val
    
    if abs(target - tree.value) < abs(closest_val - target):
        closest_val = tree.value

    if target > tree.value and tree.left != None:
        return InternalFunction(tree.right, target, closest_val)

    if target < tree.value and tree.right != None:
        return InternalFunction(tree.left, target, closest_val)
 
    return closest_val


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None