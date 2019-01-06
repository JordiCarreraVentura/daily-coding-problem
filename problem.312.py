# This problem was asked by Wayfair.
# 
# You are given a 2 x N board, and instructed to completely cover the board with the following shapes:
# 
# Dominoes, or 2 x 1 rectangles.
# Trominoes, or L-shapes.
# For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.
# 
# A B B C
# A B C C


import random

def new_board(n):
    board = []
    for row in range(2):
        board.append([None for _ in range(n)])
    return board


def cp(board):
    return [[y for y in x] for x in board]


def f(board):

    def get_possible_moves(board):
        moves = []

        def vertical_domino(board, i, j):
            # A B
            # A B
            if not i and board[i + 1][j] == None:
                return True
            return False

        def horizontal_domino(board, i, j):        
            # A A
            # B B        
            if j < len(board[i]) - 1 and board[i][j + 1] == None:
                return True
            return False
        
        def top_tromino_left(board, i, j):        
            # B B C
            # B C C
            if not i and j < len(board[0]) - 1 \
            and board[i + 1][j] == None and board[i][j + 1] == None:
                return True
            return False

        def top_tromino_right(board, i, j):        
            # B C C
            # B B C
            if not i and j < len(board[0]) - 1 \
            and board[i][j + 1] == None and board[i + 1][j + 1] == None:
                return True
            return False

        def bottom_tromino_left(board, i, j):       
            # B C C
            # B B C
            if i and j < len(board[0]) - 1 \
            and board[i - 1][j] == None and board[i][j + 1] == None:
                return True
            return False

        def bottom_tromino_right(board, i, j):       
            # B B C
            # B C C
            if i and j < len(board[0]) - 1 \
            and board[i - 1][j + 1] == None and board[i][j + 1] == None:
                return True
            return False


        for i, row in enumerate(board):
            for j, cell in enumerate(row):

                if cell != None:
                    continue
                
                # check if dominos fit
                if vertical_domino(board, i, j):
                    move = ((i, j), (i + 1, j))
                    moves.append(move)
                
                if horizontal_domino(board, i, j):
                    move = ((i, j), (i, j + 1))
                    moves.append(move)

                # check if trominos fit
                if top_tromino_left(board, i, j):
                    move = ((i, j), (i + 1, j), (i, j + 1))
                    moves.append(move)

                if top_tromino_right(board, i, j):
                    move = ((i, j), (i, j + 1), (i + 1, j + 1))
                    moves.append(move)
                
                if bottom_tromino_left(board, i, j):
                    move = ((i, j), (i - 1, j), (i, j + 1))
                    moves.append(move)

                if bottom_tromino_right(board, i, j):
                    move = ((i, j), (i - 1, j + 1), (i, j + 1))
                    moves.append(move)

        return moves


    def board_is_solved(board):
        cells = []
        for row in board:
            cells += [cell for cell in row if cell == None]
        if len(cells):
            return False
        return True

    def make_move(move, solution):
        
        def get_next_piece_id(solution):
        
            def first_gap(pieces):
                minim = 0
                maxim = max(pieces) + 2
                for x in range(minim, maxim):
                    if x not in pieces:
                        return x
        
            pieces = set([])
            for row in solution:
                pieces.update([cell for cell in row if cell != None])
            if not pieces:
                return 0
            return first_gap(pieces)
    
        next_piece_id = get_next_piece_id(solution)
        for position in move:
            row, column = position
            solution[row][column] = next_piece_id
        return solution

    def deduplicate(solutions):
    
        def get_pieces(solution):
            positions_by_id = dict([])
            for i, row in enumerate(solution):
                for j, _id in enumerate(row):
                    if not positions_by_id.has_key(_id):
                        positions_by_id[_id] = []
                    positions_by_id[_id].append((i, j))
            return tuple(sorted([
                tuple(sorted(positions)) for positions in positions_by_id.values()
            ]))
        
        def get_pieces_many(solutions):
            pieces = set([])
            for solution in solutions:
                pieces.add(get_pieces(solution))
            return pieces

        def new_solution(solution_zero):
            return [
                [None for _ in range(len(solution_zero[0]))]
                for _ in range(len(solution_zero))
            ]

        pieces = get_pieces_many(solutions)
        unique = []
        for unique_solution in pieces:
            solution = new_solution(solutions[0])
            for piece, positions in enumerate(unique_solution):
                for row, column in positions:
                    solution[row][column] = piece
            unique.append(solution)
        return unique

    if board_is_solved(board):
        return [board]
    else:
        solutions = []
        moves = get_possible_moves(board)
        if not moves:
            return []
        for move in moves:
            solution = cp(board)
            new_board = make_move(move, solution)
            solutions += f(new_board)
        return deduplicate(solutions)


if __name__ == '__main__':

   for test in range(10):
        n = random.randrange(1, 12)
#     for n in [3]:
        board = new_board(n)
        print n
        for row in board:
            print row
        print '==='
        for solution in f(board):
            for row in solution:
                print row
            print '---'
        print
