from node_class import node_obj
from heuristic import heuristic_fun
import random

class expected_minimax:
    def __init__(self, depth):
        self.depth = depth
        self.counter = 0
        self.is_maxi = True
        
    def start(self, board, C_move, last_move_color):
        self.counter = C_move + self.depth
        node, _ = self.maxi(node_obj(None, None, board, C_move , last_move_color))
        return node.index, node.board

    def maxi(self, node):
        self.is_maxi = True
        if node.C_move == 42 or node.C_move == self.counter:
            return None, self.Utility(node.board)
        
        max_child, max_utility = None, float('-inf')

        columns = list(range(7))
        random.shuffle(columns)  
        
        for index in columns:
            if node.board[index] == 0:
                child = self.get_child(node, index)
                _, utility = self.expected_value(child)

                if utility > max_utility:
                    max_child, max_utility = child, utility

        return max_child, max_utility

    def mini(self, node):
        self.is_maxi = False
        if node.C_move == 42 or node.C_move == self.counter:
            return None, self.Utility(node.board)
        
        min_child, min_utility = None, float('inf')

        columns = list(range(7))
        random.shuffle(columns)  
        
        for index in columns:
            if node.board[index] == 0:
                child = self.get_child(node, index)
                _, utility = self.expected_value(child)

                if utility < min_utility:
                    min_child, min_utility = child, utility

        return min_child, min_utility
    
    def expected_value(self,node):
        if node.C_move == 42 or node.C_move == self.counter:
            return None, self.Utility(node.board)
        
        expected_utility = 0
        probabilities=[0.2, 0.6, 0.2]
        
        if (node.index % 7) - 1 < 0:  
            probabilities = [0, 0.6, 0.4]
        elif (node.index % 7) + 1 >= 7:  
            probabilities = [0.4, 0.6, 0]
            
        for offset,probability in zip([-1,0,1],probabilities):
            index = (node.index % 7) + offset
            if 0 <= index < 7 and node.board[node.index] == 0:
                child = self.get_child(node,index)
                if self.is_maxi:
                    _,utility=self.mini(child)
                else:
                    _,utility=self.maxi(child)
                expected_utility += utility * probability
        return None,expected_utility

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

        return node_obj(None,index, board, node.C_move + 1 , color)


    def Utility(self, board):
        return heuristic_fun(board, self.player_color)