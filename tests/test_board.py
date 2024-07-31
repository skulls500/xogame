import xogame.board

def test_empty_board_has_no_winner():
    board = xogame.board.Board()
    assert board.winner() is None
