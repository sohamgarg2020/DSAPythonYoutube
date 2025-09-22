class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    

def tree_to_tuple(node):
    if node == None:
        return None
    if node.left == None and node.right == None:
        return node.key
    
    return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right))

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

"""the 3 traverse methods have been added to my github (username: sohamgarg2020) under Leetcode Problems"""

def tree_height(node):
    if node is None:
        return 0
    return 1+ max(tree_height(node.left), tree_height(node.right))

def tree_size(node):
    if node is None:
        return 1 + tree_size(node.left)+tree_size(node.right)


tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(tree2.key)
print(tree_to_tuple(tree2))