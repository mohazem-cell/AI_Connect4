class node_obj:
    def __init__(self, parent, index, board, C_move, last_move_color):
        self.value = 0
        self.parent = parent
        self.index = index
        self.board = board
        self.C_move = C_move
        self.last_move_color = last_move_color