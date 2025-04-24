def heuristic_fun(board, player_color):
    connected_2, connected_3, connected_4 = 0, 0, 0

    def check_player(index):
        if board[index] == player_color:
            return -1
        else:
            return 1

    # H
    for row in range(0,36,7):
        for col in range(row,row+6):
            if board[col] == board[col+1] and board[col] != 0:
                #2 in row
                connected_2 += check_player(col)
                if  col+2 < 42 and board[col+1] == board[col+2] and (col+2) != (row + 7):
                    #3 in row
                    connected_3 += check_player(col)
                    if col+3 < 42 and board[col+2] == board[col+3] and (col+3) != (row + 7):
                        #4 in row
                        connected_4 += check_player(col)

    # V
    for col in range(0,7):
        for row in range(col,col+29,7):
            if board[row] == board[row+7] and board[row] != 0:
                #2 in col
                connected_2 += check_player(row)
                if row+14 < 42 and board[row+7] == board[row+14] and ((row+14)%7) == (row%7):
                    #3 in col
                    connected_3 += check_player(row)
                    if row+21 < 42 and board[row+14] == board[row+21] and ((row+21)%7) == (row%7):
                        #4 in col
                        connected_4 += check_player(row)

    # D \
    for col in range(0,4):
        for row in range(col,col+29,7):
            if board[row] == board[row+8] and board[row] != 0:
                #2 in diagonal
                connected_2 += check_player(row)
                if row+16 < 42 and board[row+8] == board[row+16] and ((row+16)%7) == (((row+8)%7)+1):
                    #3 in diagonal
                    connected_3 += check_player(row)
                    if row+24 < 42 and board[row+16] == board[row+24] and ((row+24)%7) == (((row+16)%7)+1):
                        #4 in diagonal
                        connected_4 += check_player(row)

    # D /
    for col in range(3,7):
        for row in range(col,col+29,7):
            if board[row] == board[row+6] and board[row] != 0:
                #2 in diagonal
                connected_2 += check_player(row)
                if row+12 < 42 and board[row+6] == board[row+12] and ((row+12)%7) == (((row+6)%7)-1):
                    #3 in diagonal
                    connected_3 += check_player(row)
                    if row+18 < 42  and board[row+12] == board[row+18] and ((row+18)%7) == (((row+12)%7)-1):
                        #4 in diagonal
                        connected_4 += check_player(row)  

    result = connected_4 * 10000 + connected_3 * 100 + connected_2                  
    return result