from random import random


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self) -> str:
        return "<Node key={} value={}>".format(self.key, self.value)


class AVLTree:
    @staticmethod
    def height(node):
        if not node:
            return 0

        return node.height

    @staticmethod
    def get_balance(node):
        if not node:
            return 0

        return AVLTree.height(node.left) - AVLTree.height(node.right)

    def __init__(self):
        self.root = None
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def append(self, key, value):
        self.root = self._insert(self.root, key, value)
        self.length += 1

    def _insert(self, node, key, value) -> Node:
        key = str(key)

        if node is None:
            return Node(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        node.height = 1 + max(AVLTree.height(node.left), AVLTree.height(node.right))

        balance = AVLTree.get_balance(node)

        # left left case
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)

        # right right case
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)

        # left right case
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # right left cast
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _right_rotate(self, y):
        x = y.left
        t = x.right

        # perform rotation
        x.right = y
        y.left = t

        # update heights
        y.height = max(AVLTree.height(y.left), AVLTree.height(y.right)) + 1
        x.height = max(AVLTree.height(x.left), AVLTree.height(x.right)) + 1

        return x

    def _left_rotate(self, x):
        y = x.right
        t = y.left

        # perform rotation
        y.left = x
        x.right = t

        x.height = max(AVLTree.height(x.left), AVLTree.height(x.right)) + 1
        y.height = max(AVLTree.height(y.left), AVLTree.height(y.right)) + 1

        return y

    def search(self, key):
        key = str(key)
        node = self.root

        while True:
            if key == node.key:
                return node
            if node.right and key > node.key:
                node = node.right
            elif node.left and key < node.key:
                node = node.left
            else:
                return None


if __name__ == '__main__':
    t = AVLTree()

    for i in range(1, 1001):
        n = random()
        t.append(n, "value: {}".format(n))

    t.append(50, "fifty")
    t.append("some other key", "this is the content")

    print(t.root)

    print(t.search(50))
    print(t.search(-1))
    print(t.search('some other key'))

    print("tree size: {} elements".format(len(t)))
