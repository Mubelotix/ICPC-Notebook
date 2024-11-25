class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # Height of this node

class BTreeSet:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _balance(self, node):
        balance = self._balance_factor(node)
        if balance > 1: # Left heavy
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1: # Right heavy
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def insert(self, key):
        def _insert(node, key):
            if node is None:
                return TreeNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return self._balance(node) # return node if not balancing
        self.root = _insert(self.root, key)

    def remove(self, key):
        def _remove(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = _remove(node.left, key)
            elif key > node.key:
                node.right = _remove(node.right, key)
            else:
                # Node with one or no children
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                # Node with two children: find inorder successor
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.key = succ.key
                node.right = _remove(node.right, succ.key)
            return self._balance(node) # return node if not balancing
        self.root = _remove(self.root, key)

    def contains(self, key):
        def _contains(node, key):
            if node is None:
                return False
            if key < node.key:
                return _contains(node.left, key)
            elif key > node.key:
                return _contains(node.right, key)
            else:
                return True
        return _contains(self.root, key)

    def range(self, lower, upper):
        def _range(node, lower, upper):
            if node is None:
                return
            if lower is None or node.key >= lower:
                yield from _range(node.left, lower, upper)
            if (lower is None or node.key >= lower) and (upper is None or node.key < upper):
                yield node.key
            if upper is None or node.key < upper:
                yield from _range(node.right, lower, upper)
        yield from _range(self.root, lower, upper)
