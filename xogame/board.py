class Board:
    def __init__(self):
        self._board = {key: None for key in 'abcdefghi'}

    def winner(self):
        WINNING_COMBINATIONS = (
            'abc', 'def', 'ghi',
            'adg', 'beh', 'cfi',
            'aei', 'ceg'
        )

        for combination in WINNING_COMBINATIONS:
            if self._same_symbol(combination):
                return self._board[combination[0]]

        return None

    def _same_symbol(self, combination):
        first = self._board[combination[0]]
        return all(self._board[key] == first for key in combination)

    def place(self, symbol, position):
        self._board[position] = symbol
