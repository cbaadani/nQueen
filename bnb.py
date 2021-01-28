
N = 16


def print_board(board):
    for row in range(N):
        for col in range(N):
            print(board[row][col], end=" ")
        print()
    print()


# check if it possible to place the queen in the row and cow (no conflicts)
def is_possible(row, col, s_board, bs_board, s_board_state, bs_board_state, row_state):
    occupied_row = row_state[row]
    occupied_slash = s_board_state[s_board[row][col]]
    occupied_backslash = bs_board_state[bs_board[row][col]]
    if occupied_row or occupied_slash or occupied_backslash:
        return False
    return True


def solving_n_queens(board, s_board, bs_board, s_board_state, bs_board_state, row_state, col):
    if col >= N:
        return True
    for row in range(N):
        if is_possible(row, col, s_board, bs_board, s_board_state, bs_board_state, row_state):
            board[row][col] = 1
            s_board_value = s_board[row][col]
            s_board_state[s_board_value] = 1
            bs_board_value = bs_board[row][col]
            bs_board_state[bs_board_value] = 1
            row_state[row] = 1
            # recursive call
            if solving_n_queens(board, s_board,bs_board, s_board_state, bs_board_state, row_state, col + 1):
                return True
            #backtrack
            else:
                board[row][col] = 0
                s_board_state[s_board_value] = 0
                bs_board_state[bs_board_value] = 0
                row_state[row] = 0
    return False


def n_queens():
    board = [[0 for i in range(N)] for j in range(N)]
    slash_board = [[0 for i in range(N)] for j in range(N)]
    backslash_board = [[0 for i in range(N)] for j in range(N)]
    for row in range(N):
        for col in range(N):
            slash_board[row][col] = row + col
            backslash_board[row][col] = row - col + N - 1
    slash_board_state = [0]*(2*N-1)
    backslash_board_state = [0]*(2*N-1)
    row_state = [0] * N
    if solving_n_queens(board, slash_board, backslash_board, slash_board_state, backslash_board_state, row_state, 0):
        print_board(board)
        return True
    print("There is no solution")
    return False


def main():
    n_queens()


if __name__ == "__main__":
        main()
