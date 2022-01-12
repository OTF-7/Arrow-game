import math
from threading import Thread
from time import sleep

from termcolor import colored


class Game:
    def __init__(self):
        self.name = ''
        self.direction = True
        self.sleep_time = 0.03
        self.maximum = 150
        self.result = None
        self.position = 1
        self.difficulty = 1
        self.cyan_count = 0
        self.green_count = 0
        self.yellow_count = 0
        self.red_count = 0
        self.total = 0

    def play_game(self):
        try:
            self.name = input(colored('\nEnter your name > ', 'yellow'))
            self.difficulty = int(input(colored('\nEnter the level > ', "white")))
            if self.difficulty == 1:
                self.sleep_time = 0.03
            elif self.difficulty == 2:
                self.sleep_time = 0.02
            else:
                self.sleep_time = 0.01
            print("Press enter to stop...")
            self.__make_line()
            t = Thread(target=self.__start_game)
            t.start()
            self.result = input('')
            self.__show_result()
            return self.name, self.total
        except ValueError:
            print(colored("Wrong Input type, make sure that you enter an integer value!", "red"))

    def __make_line(self):
        if self.difficulty == 1:
            self.cyan_count = 0
            self.green_count = 40
            self.yellow_count = 25
            self.red_count = 20
        elif self.difficulty == 2:
            self.cyan_count = 25
            self.green_count = 25
            self.yellow_count = 15
            self.red_count = 20
        else:
            self.cyan_count = 30
            self.green_count = 25
            self.yellow_count = 15
            self.red_count = 10
        print(colored("|" * self.cyan_count, "cyan"), end='')
        print(colored("|" * self.green_count, "green"), end='')
        print(colored("|" * self.yellow_count, "yellow"), end='')
        print(colored("|" * self.red_count, "red"), end='')
        print(colored("|" * self.yellow_count, "yellow"), end='')
        print(colored("|" * self.green_count, "green"), end='')
        print(colored("|" * self.cyan_count, "cyan"))

    def __start_game(self):
        while self.result is None:
            if self.direction:
                self.__move_forward()
            else:
                self.__move_backward()

    def __move_forward(self):
        self.__move()
        self.position += 1
        if self.position == self.maximum:
            self.direction = False

    def __move_backward(self):
        self.__move()
        self.position -= 1
        if self.position == 1:
            self.direction = True

    def __move(self):
        print("\b" * self.maximum, end='')
        print(' ' * (self.position - 1), colored("^", "magenta"), sep='', end='')
        sleep(self.sleep_time)

    def __show_result(self):
        if self.difficulty == 1:
            if self.position <= self.green_count or \
                    self.position > self.green_count + self.yellow_count * 2 + self.red_count:
                self.score = 100
            elif self.position <= self.green_count + self.yellow_count or \
                    self.position > self.green_count + self.yellow_count + self.red_count:
                self.score = 200
            else:
                self.score = 300
        else:
            if self.position <= self.cyan_count or \
                    self.position > self.cyan_count + self.green_count * 2 + self.yellow_count * 2 + self.red_count:
                self.score = 100
            elif self.position <= self.cyan_count + self.green_count or \
                    self.position > self.cyan_count + self.green_count + self.yellow_count * 2 + self.red_count:
                self.score = 200
            elif self.position <= self.cyan_count + self.green_count + self.yellow_count or \
                    self.position > self.cyan_count + self.green_count + self.yellow_count + self.red_count:
                self.score = 300
            else:
                self.score = 400

        print("\b" * self.maximum, end='')
        extra = (self.maximum // 2 - math.fabs(self.maximum // 2 - self.position))
        self.total = int(self.score + extra)
        print(colored('Your score is ' + str(self.total),
                      'blue'))

    # def cut_fraction(num: float):
    #     if num.is_integer():
    #         return int(num)
    #     return num


def main():
    players = dict()
    players_list = list()
    still_playing = '1'
    try:
        while still_playing == '1':
            g = Game()
            name, total = g.play_game()
            players[name] = total
            still_playing = input(colored('Enter 1 to play again, and press enter to exit...  ', 'green'))
    except ValueError:
        print(colored("Wrong Input type, make sure that you enter an integer value!", "red"))

    for name, total in players.items():
        new_player = (total, name)
        players_list.append(new_player)

    players_list = sorted(players_list, reverse=True)

    print(colored('Best results: ', 'yellow'))
    for total, name in players_list:
        print(colored(f"{name}: {total}", "blue"))


if __name__ == '__main__':
    main()
