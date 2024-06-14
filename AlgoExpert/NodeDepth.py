# find the calculate distance for each node and them sum them all
# to find distance define a variable that can be increment each time if tree in not None
# write a internal function that takes current node and calculate the distnace
# call that function each time for the values of tree 



def nodeDepths1(root):
    # Write your code here.
    SumOfDepth = 0
    stack = [{"node" : root, "depth" : 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        SumOfDepth += depth 
        stack.append({"node":node.left, "depth":depth+1})
        stack.append({"node":node.right, "depth":depth+1})
    return SumOfDepth

def nodeDepths2(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths2(root.left, depth+1) + nodeDepths2(root.right, depth+1)




# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
