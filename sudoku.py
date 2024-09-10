import random
import time
import os

def create_board():
    base = 3
    side = base * base

    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side

    def shuffle(s):
        return random.sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    squares = side * side
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def solve_with_visualization(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(board)
            time.sleep(0.1)

            if solve_with_visualization(board):
                return True

            board[row][col] = 0
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(board)
            time.sleep(0.1)

    return False

def play_sudoku():
    board = create_board()
    print("Bem-vindo ao jogo de Sudoku!")
    print("Tabuleiro inicial:")
    print_board(board)

    while True:
        row = int(input("Digite a linha (1-9): ")) - 1
        col = int(input("Digite a coluna (1-9): ")) - 1
        num = int(input("Digite o número (1-9): "))

        if valid(board, num, (row, col)):
            board[row][col] = num
            print_board(board)
        else:
            print("Movimento inválido. Tente novamente.")

        if find_empty(board) is None:
            print("Parabéns! Você completou o Sudoku!")
            break

def main():
    while True:
        print("\n1. Jogar Sudoku")
        print("2. Resolver por força bruta")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            play_sudoku()
        elif choice == '2':
            board = create_board()
            print("Tabuleiro inicial:")
            print_board(board)
            print("\nResolvendo por força bruta...")
            solve_with_visualization(board)
            print("\nSudoku resolvido!")
        elif choice == '3':
            print("Obrigado por jogar!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()