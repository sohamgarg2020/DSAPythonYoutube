class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None



class BSTNode:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def remove_none(self, nums):
        return [x for x in nums if x is not None]

    def is_bst(self, node):
        if node is None:
            return True, None, None
        
        is_bst_l, min_l, max_l = self.is_bst(node.left)
        is_bst_r, min_r, max_r = self.is_bst(node.right)

        is_bst_node = (is_bst_l and is_bst_r and (max_l is None or node.key > max_l) and (min_r is None or node.key < min_r))

        min_key = min(self.remove_none[min_l, node.key, min_r])
        max_key = max(self.remove_none[max_l, node.key, max_r])

        return is_bst_node, min_key, max_key
    
    def insert(self, node, key, value):
        if node is None:
            node = BSTNode(key, value)
        elif key < node.key:
            node.left = self.insert(node.left, key, value)
            node.left.parent = node
        elif key > node.key:
            node.right = self.insert(node.right, key, value)
            node.right.parent = node
        return node
    
    def find(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            self.find(node.left, key)
        if key > node.key:
            self.find(node.right, key)
    
    def update(self, node, key, value):
        node = self.find(node, key)
        if node is not None:
            node.value = value

    def list_all(self, node):
        if node is None:
            return []
        return self.list_all(node.left) + [(node.key, node.value)] + self.list_all(node.right)
    
    def is_balanced(self, node):
        if node is None:
            return True, 0
        balanced_l, height_l = self.is_balanced(node.left)
        balanced_r, height_r = self.is_balanced(node.right)

        balanced = balanced_l and balanced_r and (abs(height_l-height_r)) <= 1
        height = 1+ max(height_r, height_l)

        return balanced, height
