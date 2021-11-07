# original idea by https://www.youtube.com/watch?v=k3c6dFtDqc8

board = list(range(1, 10))

wins_chord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def draw_board():
    print('+---+---+---+')
    for i in range(3):
        print('|', board[0 +i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
        print('+---+---+---+')


def take_input(player_token):
    while True:
        input_value = input(f"Введите номер клетки для {player_token} ")
        if not (input_value in "123456789"):
            print("""Ошибочный ввод. Повторите.\nВводите можно английские символы 'x' или 'o'""")
            continue
        input_value = int(input_value)
        if str(board[input_value - 1]) in "xo":
            print("Клетка уже занята")
            continue
        board[input_value - 1] = player_token
        break

def check_win():
    for i in wins_chord:
        if (board[i[0]-1]) == (board[i[1]-1]) == (board[i[2]-1]):
        # отнимаем 1 потому что нумерация позиций в board начинается с 0
            return board[i[0]-1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('x')
        else:
            take_input('o')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, " выиграл!")
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Ничья')
            break






if __name__ == '__main__':
    main()
