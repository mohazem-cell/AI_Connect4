from node_class import node_obj
from heuristic import heuristic_fun
import time

class minimax:
    def __init__(self, depth):
        self.depth = depth
        self.counter = 0

        self.player_color = None

        self.root = None
        self.tree = []

    def start(self, board, C_move, last_move_color):
        self.counter = C_move + self.depth
        self.player_color = last_move_color

        self.tree = []

        self.root = node_obj(None, None, board, C_move , last_move_color)
        self.tree.append(self.root)

        start_time = time.time() 
        node, _ = self.maxi(self.root)
        end_time = time.time()
        elapsed_time = end_time - start_time

        #self.print_tree()
        print(f"Algorithm runtime: {elapsed_time:.5f} seconds")
        print(f"nodes expanded: {len(self.tree)}")
        return node.index, node.board
    
    def print_tree(self):
        def recursive_print(node, depth=0):
            print(f"{'  ' * depth}Depth: {node.C_move}, Move: {node.index}, Value: {node.value}")
            for child in [child for child in self.tree if child.parent == node]:
                recursive_print(child, depth + 1)
    
        recursive_print(self.root)

    def maxi(self, node):
        if node.C_move == 42 or node.C_move == self.counter:
            return None, self.Utility(node.board)
        
        max_child, max_utility = None, float('-inf')

        for index in range(0, 7):
            if node.board[index] == 0:
                child = self.get_child(node, index)
                _, utility = self.mini(child)
                child.value = utility

                if utility > max_utility:
                    max_child, max_utility = child, utility

        node.value = max_utility
        return max_child, max_utility

    def mini(self, node):
        if node.C_move == 42 or node.C_move == self.counter:
            return None, self.Utility(node.board)
        
        min_child, min_utility = None, float('inf')

        for index in range(0, 7):
            if node.board[index] == 0:
                child = self.get_child(node, index)
                _, utility = self.maxi(child)
                child.value = utility

                if utility < min_utility:
                    min_child, min_utility = child, utility

        node.value = min_utility
        return min_child, min_utility

    def get_child(self, node, index):
        for row in range(35 + index, index - 1, -7):
            if node.board[row] == 0:
                index = row
                break

        if node.last_move_color == "R":
            color = "Y"
        else:
            color = "R"

        board = node.board[:]
        board[index] = color

        child = node_obj(node, index, board, node.C_move + 1 , color)
        self.tree.append(child)

        return child

    def Utility(self, board):                    
        return heuristic_fun(board, self.player_color)