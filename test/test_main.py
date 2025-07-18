import unittest

from main import create_board, make_move, check_win


class TestMain(unittest.TestCase):
    def test_vertical(self):
        board = create_board()
        make_move(board, col=0, piece='X')
        make_move(board, col=0, piece='X')
        make_move(board, col=0, piece='X')
        make_move(board, col=0, piece='X')
        self.assertTrue(check_win(board, piece='X'))

    def test_horizontal(self):
        board = create_board()
        make_move(board, col=0, piece='X')
        make_move(board, col=1, piece='X')
        make_move(board, col=2, piece='X')
        make_move(board, col=3, piece='X')
        self.assertTrue(check_win(board, piece='X'))

    def test_diagonal_left(self):
        board = create_board()
        make_move(board, col=3, piece='X')
        make_move(board, col=3, piece='O')
        make_move(board, col=3, piece='X')
        make_move(board, col=3, piece='O')
        make_move(board, col=4, piece='O')
        make_move(board, col=4, piece='X')
        make_move(board, col=4, piece='O')
        make_move(board, col=5, piece='X')
        make_move(board, col=5, piece='O')
        make_move(board, col=6, piece='O')
        self.assertTrue(check_win(board, piece='O'))

    def test_diagonal_right(self):
        board = create_board()
        make_move(board, col=3, piece='X')
        make_move(board, col=3, piece='O')
        make_move(board, col=3, piece='X')
        make_move(board, col=3, piece='O')
        make_move(board, col=2, piece='O')
        make_move(board, col=2, piece='X')
        make_move(board, col=2, piece='O')
        make_move(board, col=1, piece='X')
        make_move(board, col=1, piece='O')
        make_move(board, col=0, piece='O')
        self.assertTrue(check_win(board, piece='O'))
