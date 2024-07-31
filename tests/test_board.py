import xogame.board

def test_empty_board_has_no_winner():
    board = xogame.board.Board()
    assert board.winner() is None

def test_board_with_three_X_in_top_row_has_winner_X():
    board = xogame.board.Board()
    board.place('X', 'a')
    board.place('X', 'b')
    assert board.winner() is None
    board.place('X', 'c')
    assert board.winner() == 'X'

def test_board_game_with_X_and_O__O_wins_on_major_diagonal():
    board = xogame.board.Board()
    board.place('X', 'b')
    board.place('O', 'a')
    assert board.winner() is None

    board.place('X', 'c')
    board.place('O', 'e')
    assert board.winner() is None

    board.place('X', 'f')
    board.place('O', 'i')
    assert board.winner() == 'O'

def test_board_with_three_X_in_left_column():
    board = xogame.board.Board()
    board.place('X', 'a')
    board.place('X', 'd')
    assert board.winner() is None
    board.place('X', 'g')
    assert board.winner() == 'X'

def test_board_game_with_X_and_O__O_wins_on_minor_diagonal():
    board = xogame.board.Board()
    board.place('X', 'b')
    board.place('O', 'c')
    assert board.winner() is None

    board.place('X', 'd')
    board.place('O', 'e')
    assert board.winner() is None

    board.place('X', 'f')
    board.place('O', 'g')
    assert board.winner() == 'O'
