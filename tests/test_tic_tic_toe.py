import unittest

from tic_tac_toe import initialize_board, is_win, tally_wins

class TestTicTacToe(unittest.TestCase):

    def test_initialize_board_creates_empty_board(self):
        """Test that initialize_board function returns an empty 3x3 board."""
        self.assertEqual(initialize_board(), [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    def test_is_win_identifies_row_win(self):
        """Test that is_win function correctly identifies wins in rows."""
        board_row_win = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(is_win(board_row_win, 'X'))

    def test_is_win_identifies_column_win(self):
        """Test that is_win function correctly identifies wins in columns."""
        board_column_win = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertTrue(is_win(board_column_win, 'X'))

    def test_is_win_identifies_diagonal_win(self):
        """Test that is_win function correctly identifies wins on the diagonal"""
        board_diagonal_win = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(is_win(board_diagonal_win, 'X'))

    def test_tally_wins_counts_correct_number_of_wins(self):
        """Test that tally_wins function correctly counts the number of wins."""
        results = [True, False, True]
        self.assertEqual(tally_wins(results), 2)

# This allows running the tests by running the script
if __name__ == '__main__':
    unittest.main()

