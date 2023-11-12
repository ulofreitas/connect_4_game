###############################
# Tests (no need to change these!)

def print_board(board):
    """
    This is a helpful provided function for us to view the updated board!
    """
    column_text = "     "
    for i in range(NUM_COLUMNS):
        column_text += f"C{i} "
    print(column_text)
    for row_i in reversed(range(len(board))):
        row = board[row_i]
        current_row = f"R{row_i}: ["
        for col_i in range(len(row)):
            column = row[col_i]
            current_row += str(column)
            if col_i != len(row) - 1:
                current_row += ", "
            else:
                current_row += "]"
        print(current_row)


def test_is_valid_location_1():
    """
    Testing is_valid_location().
    """
    board = [
        [0, 0, 0, 0, 0, 0, 0 , 0],
        [0, 0, 0, 0, 0, 0, 0 , 0],
        [0, 0, 0, 0, 0, 0, 0 , 0],
        [0, 0, 0, 0, 0, 0, 0 , 0],
        [0, 0, 0, 0, 0, 0, 0 , 0],
        [0, 0, 0, 0, 0, 0, 0 , 0],
    ]
    assert is_valid_location(board, column=2) == True

def test_is_valid_location_2():
    """
    Testing is_valid_location().
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
    ]
    print_board(board)
    assert is_valid_location(board, column=1) == False

def test_is_valid_location_2():
    """
    Testing is_valid_location().
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1],
        [1, 1, 0, 0, 2, 0, 2],
        [2, 2, 0, 0, 1, 0, 2],
        [2, 1, 0, 0, 0, 0, 2],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
    ]
    print_board(board)
    assert is_valid_location(board, column=4) == True

def test_is_valid_location_3():
    """
    Testing is_valid_location().
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1],
        [1, 1, 0, 0, 2, 0, 2],
        [2, 2, 0, 0, 1, 0, 2],
        [2, 1, 0, 0, 0, 0, 2],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 2],
    ]
    print_board(board)
    assert is_valid_location(board, column=6) == False

def test_drop_piece_1():
    """
    Testing drop_piece().
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 2], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 2]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    drop_piece(board=board, row=4, column=0, piece=1)
    assert board[4][0] == 1

def test_drop_piece_2():
    """
    Testing drop_piece().
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 2], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 2]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    drop_piece(board=board, row=0, column=0, piece=2)
    assert board[0][0] == 2


def test_get_next_open_row_1():
    """
    Testing get_next_open_row(board, column).
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 2], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 2]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    row = get_next_open_row(board=board,column=0)
    assert row == 4

def test_get_next_open_row_2():
    """
    Testing get_next_open_row(board, column).
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 2], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 2]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    row = get_next_open_row(board=board,column=2)
    assert row == 0

def test_get_next_open_row_3():
    """
    Testing get_next_open_row(board, column).
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    row = get_next_open_row(board=board,column=6)
    assert row == 5

def test_not_winning_move_1():
    """
    Testing is_this_winning_move(board, piece).
    No winning move
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=1)
    assert is_winning_move == False

def test_not_winning_move_2():
    """
    Testing is_this_winning_move(board, piece).
    Not winning move
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=2)
    assert is_winning_move == False

def test_not_winning_move_3():
    """
    Testing is_this_winning_move(board, piece).
    Not winning move
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 1, 1, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 1, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=2)
    assert is_winning_move == False

def test_horizontal_winning_move_1():
    """
    Testing is_this_winning_move(board, piece).
    Horizontal winning move
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 1, 1, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 1, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=1)
    assert is_winning_move == True

def test_horizontal_winning_move_2():
    """
    Testing is_this_winning_move(board, piece).
    Horizontal winning move for player 2
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 2, 1, 2, 0, 2], #R1
        [2, 2, 2, 2, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 2, 2, 1, 0, 2]
    # R1: [1, 1, 2, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=2)
    assert is_winning_move == True

def test_horizontal_winning_move_3():
    """
    Testing is_this_winning_move(board, piece).
    Not horizontal winning move for player 1
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 2, 1, 2, 0, 2], #R1
        [2, 2, 2, 2, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 2, 2, 1, 0, 2]
    # R1: [1, 1, 2, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=1)
    assert is_winning_move == False

def test_vertical_winning_move_1():
    """
    Testing is_this_winning_move(board, piece).
    Not vertical winning move
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 2, 1, 2, 0, 2], #R1
        [2, 2, 2, 2, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 2, 2, 1, 0, 2]
    # R1: [1, 1, 2, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=1)
    assert is_winning_move == False

def test_vertical_winning_move_2():
    """
    Testing is_this_winning_move(board, piece).
    Vertical winning move for player 2
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 2, 1, 2, 0, 2], #R1
        [2, 2, 0, 2, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [2, 1, 0, 0, 0, 0, 1], #R4
        [2, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [2, 1, 0, 0, 0, 0, 0]
    # R4: [2, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 2, 1, 0, 2]
    # R1: [1, 1, 2, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=2)
    assert is_winning_move == True

def test_vertical_winning_move_3():
    """
    Testing is_this_winning_move(board, piece).
    Not Vertical winning move for player 1
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 2, 1, 2, 0, 2], #R1
        [2, 2, 0, 2, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [2, 1, 0, 0, 0, 0, 1], #R4
        [2, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [2, 1, 0, 0, 0, 0, 0]
    # R4: [2, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 2, 1, 0, 2]
    # R1: [1, 1, 2, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=1)
    assert is_winning_move == False
