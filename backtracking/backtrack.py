# Here root is the root node and path is a dynamic array
def leafpath(root, path):
    if not root and root.val == 0:
        return False
    path.append(root.val)

# Checking if the node is a leaf node 
    if not root.right and not root.left:
        return True
    
    #Now we will apply recursion
    if leafpath(root.left, path):
        return True
    if leafpath(root.right, path):
        return True
    path.pop()
    return False
    
