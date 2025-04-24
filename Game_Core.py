from Player import player_Class
from minimax import minimax
from expected_minimax import expected_minimax
from minimax_pruning import minimax_pruning

class GameCore:
    def __init__(self, player1_color, player2_color, is_AI, AI_starts, AI_Algorithm, AI_depth):
        self.Count_moves = 0
        self.board = [0] * 42

        self.is_AI = is_AI
        self.last_move_color = None
        self.turn = None

        if self.is_AI:
            if AI_Algorithm == "A":
                self.Algorithm = minimax(AI_depth)
            elif AI_Algorithm == "B":
                self.Algorithm = minimax_pruning(AI_depth)
                
            else:
                self.Algorithm = expected_minimax(AI_depth)

            if AI_starts:
                p1 = "AI"
                p2 = "player"
                self.last_move_color = player2_color
            else:
                p1 = "player"
                p2 = "AI"
        else:
            p1 = "player"
            p2 = "player"
        
        self.player1 = player_Class(p1, player1_color, True)
        self.player2 = player_Class(p2, player2_color, False)

        self.index = -1
    
    #def Start(self):
        #not used
        #while self.Count_moves < 42:
        #    col = input("Choose Col from 1 to 7: ")
        #    col = int(col)
        #    self.Move(col-1)

        #self.Update_win_counts()
        #self.Determine_winner()

    def AI_Move(self):
        index, board = self.Algorithm.start(self.board, self.Count_moves, self.last_move_color)
        self.board = board
        self.Count_moves += 1
        self.player1.Turn = not (self.player1.Turn)
        self.player2.Turn = not (self.player2.Turn)
        #self.Print_board()
        #print(index)
        #print(self.Count_moves)
        return index

    def Move(self, col):
        if self.board[col] == 0:
            for row in range(35 + col, col - 1, -7):
                if self.board[row] == 0:
                    if self.player1.Turn:
                        self.board[row] = self.player1.Color
                        self.last_move_color = self.player1.Color
                        self.turn = 1
                    else: 
                        self.board[row] = self.player2.Color
                        self.last_move_color = self.player2.Color
                        self.turn = 2
                    self.Count_moves += 1
                    self.player1.Turn = not (self.player1.Turn)
                    self.player2.Turn = not (self.player2.Turn)
                    return row, self.turn
        return -1, -1

    #def Print_board(self):
    #    #not used
    #    for i in range(0,42):
    #        print(self.board[i] , " ", end="")
    #        if i % 7 == 6:
    #            print("\n")

    def Update_win_counts(self):
        self.player1.C_win = self.Check_win(self.player1.Color)
        self.player2.C_win = self.Check_win(self.player2.Color)

    def Check_win(self,color_value):
        count=0

        for row in range(6):  # Horizontal
            for col in range(4):
                if all(self.board[row * 7 + col + i] == color_value for i in range(4)):
                    count += 1

        for col in range(7):  # Vertical
            for row in range(3):
                if all(self.board[(row + i) * 7 + col] == color_value for i in range(4)):
                    count += 1

        for row in range(3):  # Diagonal /
            for col in range(4):
                if all(self.board[(row + i) * 7 + col + i] == color_value for i in range(4)):
                    count += 1

        for row in range(3):  # Diagonal \
            for col in range(4):
                if all(self.board[(row + 3 - i) * 7 + col + i] == color_value for i in range(4)):
                    count += 1
        
        return count

    def Determine_winner(self):
        if self.player1.C_win > self.player2.C_win:
            return 1, self.player1.C_win
        elif self.player2.C_win > self.player1.C_win:
            return 2, self.player2.C_win
        else:
            return 0, self.player1.C_win

#game = GameCore()