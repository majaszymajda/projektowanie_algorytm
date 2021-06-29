import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from lista4_zad0 import Robot


class BST_class:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.root = None
        self.value = value
        self.edgeBase = []

    def insert(self, value, path):
        path.append(self.value)
        if not self.value:
            self.value = value
            self.root = value
            return path

        if self.value == value:
            return path

        if value < self.value:
            if self.left:
                self.left.insert(value, path)
                return path
            self.left = BST_class(value)
            return path

        if self.right:
            self.right.insert(value, path)
            return path
        self.right = BST_class(value)
        return path

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.value

    def delete(self, value):
        if self == None:
            return self
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
            return self
        if value > self.value:
            if self.right:
                self.right = self.right.delete(value)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.value = min_larger_node.value
        self.right = self.right.delete(min_larger_node.value)
        return self

    def exists(self, value):
        if value == self.value:
            return True

        if value < self.value:
            if self.left == None:
                return False
            return self.left.exists(value)

        if self.right == None:
            return False
        return self.right.exists(value)

    def preorder(self, vals):
        if self.value is not None:
            vals.append(self.value)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.value is not None:
            vals.append(self.value)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.value is not None:
            vals.append(self.value)
        return vals

    def showRoot(self):
        return self.root

    def storeEdges(self, node, path):
        if path[-1] != None and path[-1] != node:
            self.edgeBase.append((node, path[-1]))

    def giveEdges(self):
        return self.edgeBase

    def generateGraph(self):
        nodes = self.postorder([])
        edges = self.giveEdges()
        G = nx.Graph()
        for node in nodes:
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge[0], edge[1])
        pos = nx.spring_layout(G)
        nx.draw(G, pos, node_size = 500, with_labels=1)
        plt.show()


TASK_NUMBER = 2
robots = Robot()
# robotsArmy = robots.raiseArmy(HOW_MANY_ROBOTS)
robotsArmy = robots.openArmy()
print(robotsArmy)
nodes = [34, 18, 13, 50, 44, 22, 13, 19, 48, 45, 20]

if TASK_NUMBER == 2:
    keyParam = ''
    while keyParam not in ['masa', 'zasieg', 'rozdz']:
        keyParam = input('Według jakiego parametra tworzyć? Odp: ')
        if keyParam == '':
            break
        if keyParam not in ['masa', 'zasieg', 'rozdz']:
            print('Nie o to chodzi, do wyboru: "masa", "zasieg", "rozdz"')

    if keyParam != '':
        keyParamValues = []
        for elem in robotsArmy:
            keyParamValues.append(elem[keyParam])

        nodes = keyParamValues.copy()

bst = BST_class()
for node in nodes:
    path = bst.insert(node, [])
    # print(f'{node} => {path}\n')
    bst.storeEdges(node, path)

print(bst.giveEdges())
bst.generateGraph()

print(f'Root: {bst.showRoot()}\n')

print(f"in-order:\n{bst.inorder([])}\n")
print(f"post-order:\n{bst.postorder([])}\n")
print(f"pre-order:\n{bst.preorder([])}\n")

nodesForDelate = [11, 20, 48]
print("deleting " + str(nodesForDelate))
for node in nodesForDelate:
    bst.delete(node)

print(f"34 exists: {bst.exists(34)}")
print(f"11 exists: {bst.exists(11)}")
print(f"20 exists: {bst.exists(20)}")
print(f"48 exists: {bst.exists(48)}")
print(f"45 exists: {bst.exists(45)}")
print(f"18 exists: {bst.exists(18)}")

print(f"in-order:\n{bst.inorder([])}\n")
print(f"post-order:\n{bst.postorder([])}\n")
print(f"pre-order:\n{bst.preorder([])}\n")