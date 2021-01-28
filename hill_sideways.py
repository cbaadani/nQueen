import random

N = 16


def random_board():
    board = list([random.randint(0, N-1) for x in range(N)])
    return board


# clculate the number of conflicts
def num_of_conflicts(state):
    conflicts = 0
    for curr_queen in range(N):
        for other_queen in range(curr_queen + 1, N):
            if state[curr_queen] == state[other_queen]:
                conflicts += 1
            if abs(state[curr_queen] - state[other_queen]) == (other_queen - curr_queen):
                conflicts += 1
    return conflicts


def n_queens():
    board = random_board()
    sideways = 30
    while num_of_conflicts(board) > 0:
        curr_num_conflicts = num_of_conflicts(board)
        successors = {}
        possible_steps = []
        for col in range(N):
            for row in range(N):
                if board[col] == row:
                    continue
                copy_state = board.copy()
                copy_state[col] = row
                successors[(col, row)] = num_of_conflicts(copy_state)
        min_num_conflicts = sorted(successors.values())[0]
        new_state = board.copy()
        if min_num_conflicts <= curr_num_conflicts:
            for key, value in successors.items():
                if value == min_num_conflicts:
                    possible_steps.append(key)
            len_pos = len(possible_steps)
            if len_pos > 0:
                x = random.randint(0, len_pos - 1)
                col = possible_steps[x][0]
                row = possible_steps[x][1]
                new_state[col] = row
            # check the num of sideways
            if min_num_conflicts == curr_num_conflicts:
                sideways -= 1
        if new_state == board or sideways == 0:
            print("stuck, no solution")
            return False
        board = new_state
    print_board(board)
    return True


def print_board(board):
    for col in range(N):
        for row in range(N):
            if board[col] == row:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
    print()


def main():
    n_queens()


if __name__ == "__main__":
        main()
