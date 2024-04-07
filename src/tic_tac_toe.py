'''A buggy Tic-Tac-Toe game that provides an opportunity to debug code by both reasoning about it and stepping through it in a debugger.

The program has a number of bugs that are introduced one at a time. The goal is to find and fix the bugs.

Ensure you step through this program in an IDE debugger and pdb to understand how the program works and to find the bugs.'''

def initialize_board():
    '''Initialises a 2d data structure consisting of 3 x 3 grid of blank spaces'''
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    '''
        Prints the Game board based on the range specified in the global 'board' variable

        Parameter
        ---------
        board (2d data structure) : Represents the game board as a 3 x 3 grid

        Returns
        -------
        Print statements : Based on iterations through the range defined in the 'board' variable

        Example
        -------
        #>>> board = [[' ' for _ in range(3)] for _ in range(3)]
        #>>> print_board()
         | |
        -----
         | |
        -----
         | |
        -----
    '''
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def _check_rows(board, player):
    ''' Check rows for win condition for a given player.

        Parameter(s)
        ---------
        board (2d data structure) : Represents the game board as a 3 x 3 grid
        player (string) : Represents the current player 'X' or 'O'

        Returns
        ---------
        Boolean : True (if an entire row consists of the same 'string' character), else False (if it does not)

        Example
        --------
        #>>> board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        #>>> player = 'X'
        #>>> _check_rows(board, player)
        return True
    '''
    for i in range(3):
        if all([cell == player for cell in board[i]]):  
            return True
    return False

def _check_columns(board, player):
    '''Check columns for win condition for a given player.

    Parameter(s)
    ------------
    board (2d data structure) : Represents the game board as a 3 x 3 grid
    player (string) : Represents the current player 'X' or 'O'

    Returns
    ---------
    Boolean : True (if an entire column consists of the same 'string' character), else False (if it does not)

    Example
    --------
    #>>> board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
    #>>> player = 'X'
    #>>> _check_rows(board, player)
    True
    '''
    for i in range(3):
        if all([board[j][i] == player for j in range(3)]):  
            return True
    return False

def _check_diagonals(board, player):
    '''Check diagonals for win condition for a given player.

    Parameter
    ---------
    board (2d data structure) : Represents the game board as a 3 x 3 grid
    player (string) : Represents the current player 'X' or 'O'

    Returns
    ---------
    Boolean : True (if the diagonal win condition is met), else False (if it is not)

    Example
    --------
    #>>> board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
    #>>> player = 'X'
    #>>> _check_rows(board, player)
    True
    '''
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_win(board, player):
    '''Check rows, columns, and diagonals for win condition for a given player.
    Parameter
    ---------
    board (2d data structure) : Represents the game board as a 3 x 3 grid
    player (string) : Represents the current player 'X' or 'O'

    Returns
    ---------
    Boolean : True (if the player has met the conditions for win in any of the methods listed - Row, Column or Diagonal)
                False if it does not

    Example
    --------
    #>>> board = [[' ', ' ', 'X'], [' ', 'X', ' '], ['X', ' ', ' ']]
    #>>> player = 'X'
    #>>> _check_rows(board, player)
    True
    '''
    return _check_rows(board, player) or _check_columns(board, player) or _check_diagonals(board, player)

def tally_wins(results):
    '''Count the number of wins.

    Parameter
    ---------
    results (list) : List of booleans representing the number of moves made to win the game. Converted to integers by
    using pythons True = 1 and False = 0 it represents the number of won games.

    Returns
    --------
    Integer: The sum of the results list leveraging pythons True = 1 and False = 0 it returns the number of games won

    Examples
    ---------
    #>>> tally_wins([False, False, False, False, True])
    1
    '''
    return sum(results)

# def main():
#     board = initialize_board()
#     current_player = 'X'
#     moves = 0
#     results = []
#
#     while moves < 9:
#         print_board(board)
#         row, col = map(int, input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())
#         if board[row][col] == ' ':
#             board[row][col] = current_player
#             win = is_win(board, current_player)
#             results.append(win)
#             if win:
#                 print_board(board)
#                 print(f"Player {current_player} wins!")
#                 return
#             current_player = 'O' if current_player == 'X' else 'X'
#             moves += 1
#         else:
#             print("Cell already occupied! Try again.")
#     print_board(board)
#     print("It's a draw!")
#     print(f"Number of wins during the game: {tally_wins(results)}")
#
# if __name__ == "__main__":
#     main()

