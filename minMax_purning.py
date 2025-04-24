# from Game_Core import GameCore

class minMax_purn:
    def __init__(self,GameCore):
        self.game = GameCore

    def terminal_test(self):
        return self.game.Count_moves == 42

    def evaluate(self,board,color_value):
        score = 0
        opponent_color = 1 if color_value == 2 else 2

        def evaluate_line(line):
            nonlocal score
            line_count = line.count(color_value)
            opponent_count = line.count(opponent_color)

            if line_count > 0 and opponent_count == 0:
                score += {4: 1000, 3: 50, 2: 10}.get(line_count, 0)
            elif opponent_count > 0 and line_count == 0:
                score -= {4: 1000, 3: 50, 2: 10}.get(opponent_count, 0)

        for row in range(6):  # Horizontal
            for col in range(4):
                evaluate_line([board[row * 7 + col + i] for i in range(4)])

        for col in range(7):  # Vertical
            for row in range(3):
                evaluate_line([board[(row + i) * 7 + col] for i in range(4)])

        for row in range(3):  # Diagonal /
            for col in range(4):
                evaluate_line([board[(row + i) * 7 + col + i] for i in range(4)])

        for row in range(3):  # Diagonal \
            for col in range(4):
                evaluate_line([board[(row + 3 - i) * 7 + col + i] for i in range(4)])

        return score

    def children(self):
        return [col for col in range(7) if self.game.is_Empy(col)]

    def simulateMove(self,board,col,color):
        for row in range(35 + col, col - 1, -7):
            if board[row] == 0:
                board[row] = color
                break

    def DECISION(self,board,depth,maximizingPlayer):
        _, bestMove = self.MAXIMIZE(board, depth, float('-inf'), float('inf'), maximizingPlayer)
        return bestMove

    def MINIMIZE(self,board,depth,alpha,beta,maximizingPlayer):
        if depth ==0 or self.terminal_test():
            return self.evaluate(board, 1 if maximizingPlayer else 2),None
        minChild=None
        minUtility=float('inf')
        for child in self.children():
            newBoard = board[:]
            self.simulateMove(newBoard, child, 1 if maximizingPlayer else 2)

            utility, _ = self.MAXIMIZE(newBoard, depth - 1, alpha, beta, not maximizingPlayer)

            if utility < minUtility:
                minUtility = utility
                minChild = child

            beta = min(beta, minUtility)
            if beta <= alpha:
                break

        return minUtility, minChild

    def MAXIMIZE(self,board,depth,alpha,beta,maximizingPlayer):
        if depth==0 or self.terminal_test():
            return self.evaluate(board, 1 if maximizingPlayer else 2),None
        maxChild=None
        maxUtility=float('-inf')

        for child in self.children():
            newBoard=board[:]

            self.simulateMove(newBoard, child, 1 if maximizingPlayer else 2)
            utility, _ = self.MINIMIZE(newBoard, depth - 1, alpha, beta, not maximizingPlayer)
            if utility > maxUtility:
                maxUtility = utility
                maxChild = child

            alpha = max(alpha, maxUtility)
            if beta <= alpha:
                break
        return maxUtility, maxChild