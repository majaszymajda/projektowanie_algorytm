import networkx as nx
import sys
import math


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data >= self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def delete(self, data):
        if data is None:
            return data
        if data < self.data:
            self.left.delete(self.left, data)
        elif data > self.data:
            self.right.delete(self.right, data)

        else:
            if self.left is None:
                temp = self.right
                data = None
                return temp
            elif self.right is None:
                temp = self.left
                root = None
                return temp

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()

        if self.right:
            self.right.PrintTree()


def isBST(root):
    if root == None or (root.left == None and root.right == None):
        return True

    if root.right:
        return root.data > root.left.data

    elif root.right:
        return root.data <= root.right.data

    return isBST(root.left) and isBST(root.right)

COUNT = 10


def print2DUtil(root, space):

    if root == None:
        return

    space += COUNT
    print2DUtil(root.right, space)
    for i in range(COUNT, space):
        print(end=" ")
    print(root.data)

    print2DUtil(root.left, space)


def print2D(root):
    print2DUtil(root, 0)


def correctBstUtil(root, first, middle, last, prev):
    if root:
        correctBstUtil(root.left, first, middle, last, prev)

        if prev[0] and root.data < prev[0].data:
            if not first[0]:
                first[0] = prev[0]
                middle[0] = root
            else:
                last[0] = root

        prev[0] = root

        correctBstUtil(root.right, first, middle, last, prev)


def correctBst(root):
    first = [None]
    middle = [None]
    last = [None]
    prev = [None]
    correctBstUtil(root, first, middle, last, prev)

    if first[0] and last[0]:

        first[0].data, last[0].data = (last[0].data, first[0].data)

    elif (first[0] and middle[0]):

        first[0].data, middle[0].data = (middle[0].data,
                                       first[0].data)


def storeBSTNodes(root, nodes):
    if not root:
        return

    storeBSTNodes(root.left, nodes)
    nodes.append(root)
    storeBSTNodes(root.right, nodes)


def buildTreeUtil(nodes, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    node = nodes[mid]

    node.left = buildTreeUtil(nodes, start, mid - 1)
    node.right = buildTreeUtil(nodes, mid + 1, end)
    return node


def buildTree(root):
    nodes = []
    storeBSTNodes(root, nodes)

    n = len(nodes)
    return buildTreeUtil(nodes, 0, n - 1)


nodes = [7, 1, 5, 0, 9, 10, 4]
print(nodes)

root = Node(6)
for i in nodes:
    root.insert(i)


root.PrintTree()

root = buildTree(root)
# root.left = Node(20)
# root.left.right.left = Node(50)
root.right.left = Node(1)
print(isBST(root))
print2D(root)
# correctBst(root)
# print(isBST(root))
# print(isBST(root))#
# print2D(root)

