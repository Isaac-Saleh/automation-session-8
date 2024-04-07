from tic_tac_toe import initialize_board
from tic_tac_toe import print_board
from tic_tac_toe import is_win
from tic_tac_toe import tally_wins


def main():
    board = initialize_board()
    current_player = 'X'
    moves = 0
    results = []

    while moves < 9:
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())
        if board[row][col] == ' ':
            board[row][col] = current_player
            win = is_win(board, current_player)
            results.append(win)
            if win:
                print_board(board)
                print(f"Player {current_player} wins!")
                return
            current_player = 'O' if current_player == 'X' else 'X'
            moves += 1
        else:
            print("Cell already occupied! Try again.")
    print_board(board)
    print("It's a draw!")
    print(f"Number of wins during the game: {tally_wins(results)}")


if __name__ == "__main__":
    main()
