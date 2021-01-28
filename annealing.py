import random
import math


N = 16
TEMPERATURE = 200000


def random_board():
    board = list([random.randint(0, N-1) for x in range(N)])
    return board


def num_of_conflicts(state):
    conflicts = 0
    for curr_queen in range(N):
        for other_queen in range(curr_queen + 1, N):
            if state[curr_queen] == state[other_queen]:
                conflicts += 1
            if abs(state[curr_queen] - state[other_queen]) == (other_queen - curr_queen):
                conflicts += 1
    return conflicts


def simulated_annealing():
    solution_found = False
    curr_state = random_board()
    curr_num_conflicts = num_of_conflicts(curr_state)
    t = TEMPERATURE
    # cooling rate
    sch = 0.99
    iterations = 100000

    while t > 0 and iterations > 0:
        successor = curr_state.copy()
        col = random.randint(0, N - 1)
        row = random.randint(0, N - 1)
        successor[col] = row
        successor_conflicts = num_of_conflicts(successor)
        delta = successor_conflicts - curr_num_conflicts
        # check if the neighbor is better or the propability is bigger then random prop
        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / t):
            curr_state = successor.copy()
            curr_num_conflicts = num_of_conflicts(curr_state)
            t *= sch
            iterations -= 1
        if curr_num_conflicts == 0:
            solution_found = True
            print_board(curr_state)
            break
    if solution_found is False:
        print("Failed")


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
    simulated_annealing()


if __name__ == "__main__":
        main()
