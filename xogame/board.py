class Board:
    def __init__(self):
        self._board = {key: None for key in 'abcdefghi'}

    def winner(self):
        for row in ('abc', 'def', 'ghi'):
            if self._board[row[0]] == self._board[row[1]] == self._board[row[2]]:
                return self._board[row[0]]

        for column in ('adg', 'beh', 'cfi'):
            if self._board[column[0]] == self._board[column[1]] == self._board[column[2]]:
                return self._board[column[0]]

        if self._board['a'] == self._board['e'] == self._board['i']:
            return self._board['a']

        if self._board['c'] == self._board['e'] == self._board['g']:
            return self._board['c']

    def place(self, symbol, position):
        self._board[position] = symbol
