import numpy as np
from random import randint as random

WHITE = 0
GREY = 1
BLACK = 2


class Node:
    def __init__(self):
        self.colour = WHITE
        self.parent = None
        self.sons = []
        self.discover_time = None
        self.end_time = None

    def add_son(self, node):
        self.sons.append(node)


class Graph:
    def __init__(self, nodes, arcs):
        self.nodes = [None] * nodes
        for i in xrange(nodes):
            self.nodes[i] = Node()

        self.adjacency_matrix = self.generate_matrix(nodes, arcs)

        for i in xrange(nodes):
            for j in xrange(nodes):
                if self.adjacency_matrix[i][j] == 1:
                    self.nodes[i].add_son(self.nodes[j])

    def transpose(self):
        self.adjacency_matrix = np.transpose(self.adjacency_matrix)

        for node in self.nodes:
            node.sons = []

        num_of_nodes = len(self.nodes)

        for i in xrange(num_of_nodes):
            for j in xrange(num_of_nodes):
                if self.adjacency_matrix[i][j] == 1:
                    self.nodes[i].add_son(self.nodes[j])

    @staticmethod
    def generate_matrix(nodes, arcs):
        assert arcs <= nodes ** 2
        matrix = np.zeros([nodes, nodes], int)
        for i in xrange(arcs):
            row = random(0, nodes - 1)
            col = random(0, nodes - 1)

            while matrix[row][col] == 1:
                row = random(0, nodes - 1)
                col = random(0, nodes - 1)
            matrix[row][col] = 1
        return matrix
