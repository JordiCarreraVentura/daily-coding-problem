# This problem was asked by Salesforce.
# 
# Connect 4 is a game where opponents take turns dropping red or black discs into a 7 x 6 vertically suspended grid. The game ends either when one player creates a line of four consecutive discs of their color (horizontally, vertically, or diagonally), or when there are no more spots left in the grid.
# 
# Design and implement Connect 4.


import random


def make_board():
    return [
        [None for i in range(6)]
        for i in range(7)
    ]


def end_game(player1, player2, board):
    
    def is_full(board):
        full = 0
        for row in board:
            full += len([cell for cell in row if cell != None])
        if full == 42:
            return True
        return False
    
    def player_wins(player, board):
        # check horizontally
        for row in board:
            for i in range(len(row) - 3):
                if row[i:i + 4] == [player] * 4:
                    return True

        # check vertically
        cols = [
            [row[i] for row in board]
            for i in range(len(board[0]))
        ]
        for col in cols:
            for i in range(len(col) - 3):
                if col[i:i + 4] == [player] * 4:
                    return True

        # check diagonally

        ##  bottom-up, left-right
        l = len(board)
        _l = len(board[0])
        for m in range(6, -1, -1):
            if m - 4 < 0:
                break
            for n in range(0, _l):
                if n + 4 > _l:
                    break
                diagonal = [
                    board[m][n]
                ] + [
                    board[m - i][n + i]
                    for i in range(1, 4)
                ]
                if diagonal == [player] * 4:
                    return True

        ##  top-down, left-right
        for m in range(0, l):
            if m + 4 > l:
                break
            for n in range(0, _l):
                if n + 4 > _l:
                    break
                diagonal = [
                    board[m][n]
                ] + [
                    board[m + i][n + i]
                    for i in range(1, 4)
                ]
                if diagonal == [player] * 4:
                    return True
        
        return False

    print 'end_game'
    if is_full(board):
        print 'end_game.is_full'
        return True, None
    
    if player_wins(player1, board):
        print 'end_game.player1'
        return True, player1
    
    if player_wins(player2, board):
        print 'end_game.player2'
        return True, player2
    
    return False, None


def can_move(player, move, board):
    m, n = move
    if board[m][n] == None \
    and (m == len(board) - 1 \
    or board[m + 1][n] != None):
        return True
    return False


def pc_move(player, board):
    while True:
        move = (random.randrange(0, 7), random.randrange(0, 6)) # M x N
        if can_move(player, move, board):
            return move


def user_move(player, board):
    display(board)
    while True:
        q = raw_input('move? (%s) (15,56, ...)>' % player)
        if not q:
            exit()
        try:
            m, n = list(q)
            m, n = (len(board) - 1) - int(m), int(n)
            if can_move(player, (m, n), board):
                return (m, n)
        except Exception:
            continue


def apply_move(player, move, board):
    m, n = move
    try:
        board[m][n] = player
    except IndexError:
        return


def is_win(status, winner):
    if status:
        if winner != None:
            print winner
        return True
    return False


def display(board):
    print range(len(board[0]))
    for i, row in enumerate(board):
        print [len(board) - (i + 1)] + row
    


if __name__ == '__main__':

    board = make_board()
    
    player1 = True if random.random() >= 0.5 else False
    player2 = False if player1 == True else True

    while True:

        if player1:
            move = user_move(player1, board)
            apply_move(player1, move, board)
            status, winner = end_game(player1, player2, board)
            if is_win(status, winner):
                break

            move = pc_move(player2, board)
            apply_move(player2, move, board)

        else:
            move = pc_move(player1, board)
            apply_move(player1, move, board)
            status, winner = end_game(player1, player2, board)
            if is_win(status, winner):
                break

            move = user_move(player2, board)
            apply_move(player2, move, board)

        status, winner = end_game(player1, player2, board)
        if is_win(status, winner):
            break
    
    display(board)
