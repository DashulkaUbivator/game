# class Board:
#     def __init__(self):
#         self.cell = list('0' for _ in range(1, 10))
#     def change_cell(self, number):
#         if number is '0':
#             self.cell[number] = choice
#             print('Текущее поле')
#             for i in range(len(self.cell)):
#                 if (i + 1) % 3 == 0:
#                     print(self.cell[i])
#                     print('\n')
#                 else:
#                     print(self.cell[i], end=' ')
#             return True
#         else:
#             return False
#     def is_end(self):
#         pass
#
# class Cell:
#     def __init__(self, is_empty, number, symbol):
#         self.is_empty = is_empty
#         self.number = number
#         self.symbol = symbol
#
# class Player:
#     wins = 0
#     def __init__(self, name, sym):
#         self.name = name
#         self.sym = sym
#     def make_move(self):
#         flag = False
#         while not flag:
#             try:
#                 player_move = int(input(f'Куда поставим {self.sym}?'))
#             except:
#                 print('Введите число!')
#                 continue
#             if 1 <= player_move <= 9:
#                 if
#
#         return Field.number
#
# class Game:
#     def __init__(self, game_state, players):
#         self.game_state = game_state
#         self.players = players
#         self.board = Board()
#     def one_move(self, player):
#         cell_num = int(input('Введите номер клетки: '))
#         Board.change_cell(cell_num)
#         # if
#
#
# player_1 = Player('Kate')
# player_2 = Player('Ann')

# class Board:
#     board = list(range(1, 10))
#     win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     def print_board(self):
#         for cell in range(3):
#             print(self.board[0 + cell * 3], self.board[1 + cell * 3], self.board[2 + cell * 3])
#     def change_cell(self):
#         if str(self.board[Player.move() - 1]) not in 'XO':
#             self.board[Player.move() - 1] = Player.symbol
#         else:
#             print('Клетка уже занята')
#     def check_win(self):
#         for each in self.win_coord:
#             if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
#                 return self.board[each[0]]
#         return False
#
# class Player:
#     def __init__(self, symbol, name, wins):
#         self.name = name
#         self.wins = wins
#         self.symbol = symbol
#     def move(self):
#         valid = False
#         while not valid:
#             player_answer = input("Куда поставим " + self.symbol + '? ')
#             try:
#                 player_answer = int(player_answer)
#             except:
#                 print('Некорректный ввод числа')
#                 continue
#             if 1 <= player_answer <= 9:
#                 return player_answer
#             else:
#                 print('Введите число от 1 до 9')
#
#
# def game(name):
#     board = Board()
#     counter = 0
#     win = False
#     while not win:
#         board.print_board()
#         if counter % 2 == 0:
#             Player('X', name).move()
#         else:
#             Player('O', name).move()
#         counter += 1
#         if counter > 4:
#             tmp = Board.check_win()
#             if tmp:
#                 print(tmp, 'выиграл')
#                 win = True
#                 break
#         if counter == 9:
#             print('Ничья')
#             break
#     board.print_board()
#
# name = input('Введите имя игрока ')
# game(name)
# input('Нажмите Enter для выхода!')

class Board:
    board = list(range(1, 10))
    def print_board(self):
        for cell in range(3):
            print(self.board[0 + cell * 3], self.board[1 + cell * 3], self.board[2 + cell * 3])

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    def move(self):
        valid = False
        while not valid:
            player_answer = input(self.name + ' куда поставим ' + self.symbol + '? ')
            try:
                player_answer = int(player_answer)
            except:
                print('Некорректный ввод числа')
                continue
            if 1 <= player_answer <= 9:
                if str(Board.board[player_answer - 1]) not in 'XO':
                    Board.board[player_answer - 1] = self.symbol
                    valid = True
                else:
                    print('Эта клетка уже занята')
            else:
                print('Некорректно. Введите число от 1 до 9')
class Win:
    def __init__(self):
        self.win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    def check_win(self):
        for each in self.win_coord:
            if Board.board[each[0]] == Board.board[each[1]] == Board.board[each[2]]:
                return Board.board[each[0]]
        return False

class Game:
    name_1 = input('Введите имя первого игрока ')
    name_2 = input('Введите имя второго игрока ')
    def one_move(self):
        board = Board()
        board.print_board()
        Player(self.name_1, 'X').move()
        board.print_board()
    def one_game(self):
        board = Board()
        counter = 0
        result = Win()
        while True:
            board.print_board()
            if counter % 2 == 0:
                Player(self.name_1, 'X').move()
            else:
                Player(self.name_2, 'O').move()
            counter += 1
            if counter > 4:
                winner = result.check_win()
                if winner == 'X':
                    print(self.name_1, 'выиграл(a)')
                    return 'X'
                else:
                    print(self.name_2, 'выиграл(a)')
                    return 'O'
            if counter == 9:
                print('Ничья')
                break
    def tournament(self):
        x_wins = 0
        o_wins = 0
        while True:
            score = self.one_game()
            if score == 'X':
                x_wins += 1
            elif score == 'O':
                o_wins += 1
            print('Счет:', x_wins, ':', o_wins)
            one_more_time = input('Сыграть еще раз? ')
            if one_more_time == 'yes' or 'да' or 'YES' or 'ДА' or 'Yes' or 'Да' or 'Y' or 'y':
                continue
            else:
                break

mode = 0
game = Game()
while True:
    mode = int(input('Выберите режим игры (1 - один ход, 2 - одна игра, 3 - серия игр) '))
    if mode == 1:
        game.one_move()
        break
    elif mode == 2:
        game.one_game()
        break
    elif mode == 3:
        game.tournament()
        break
