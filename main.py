import os
from threading import Thread
from time import sleep

from terminal_colors import *
from art import *
import winsound


class Game:
    def __init__(self):
        # The name of the player
        self.name = ''
        # The direction of the arrow (from the left to the right and from the right to the left)
        self.direction = True
        # Time between arrow movements
        self.sleep_time = 0.03
        # Maximum number of slashes
        self.maximum = 150
        # The arrow keep moving until the user enter a value to the finish_game variable (or just press enter)
        self.finish_game = None
        # The position of the arrow
        self.position = 1
        # The level of the game
        self.difficulty = 1
        # Number of cyan slashes
        self.cyan_count = 0
        # Number of green slashes
        self.green_count = 0
        # Number of yellow slashes
        self.yellow_count = 0
        # Number of red slashes
        self.red_count = 0
        # The score of the player
        self.total = 0
        self.high = 400
        self.low = 200

    def play_game(self):
        """Public method: for starting the game"""
        # For supporting windows system colors
        os.system("color")

        # The name of the player
        self.name = input(Fore.WHITE + '\nEnter your name > ' + Fore.RESET)
        # If the user entered non numeric value, he will be prompt to enter another
        while self.name == "":
            self.name = input(Fore.YELLOW + '\nYou should enter your name > ' + Fore.RESET)

        # The level of the game
        user_input = input(Fore.WHITE + '\nEnter the level > ' + Fore.RESET)
        # If the user entered non numeric value, he will be prompt to enter another
        while not user_input.isdigit() or (user_input.isdigit() and int(user_input) not in [1, 2, 3]):
            user_input = input(
                Fore.YELLOW + '\nWrong input type, The level should be 1, 2, or 3, try again > ' + Fore.RESET)
        self.difficulty = int(user_input)

        # Change the duration according to the level of the game
        if self.difficulty == 1:
            self.sleep_time = 0.03
        elif self.difficulty == 2:
            self.sleep_time = 0.02
        else:
            self.sleep_time = 0.01

        # Start drawing the goal
        print(Fore.BLUE + """
Press enter to stop...
              """ + Fore.RESET)
        self.__draw_goal()

        # Thread for moving the arrow
        t = Thread(target=self.__start_game)
        t.start()
        # The main thread is waiting for an input from the user
        self.finish_game = input('')
        # After pressing the enter button, __show_result() method will be invoked
        self.__show_result()
        # After completing one game, it will return the name and the result of the player
        return self.name, self.total

    def __draw_goal(self):
        """Private method: for drawing the goal"""
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

        # for printing the points numbers
        for index in range(150):
            if index % 5 == 0:
                if index == 0 or index == 75 or index == 150 or index == 25 \
                        or index == 50 or index == 100 or index == 125:
                    color = Fore.BLACK
                else:
                    color = Fore.WHITE
                print(color + str(index + 1), end=' ' * (5 - len(str(index))))
        print("\b" + Fore.BLACK + "150")

        for index in range(150):
            if index % 5 == 0:
                if index == 0 or index == 75 or index == 150 or index == 25 \
                        or index == 50 or index == 100 or index == 125:
                    color = Fore.BLACK
                else:
                    color = Fore.WHITE
                print(color + "*", end=' ' * 4)
        print("\b" + Fore.BLACK + "*")

        print(Fore.CYAN + "|" * self.cyan_count + Fore.RESET, end='')
        print(Fore.GREEN + "|" * self.green_count + Fore.RESET, end='')
        print(Fore.YELLOW + "|" * self.yellow_count + Fore.RESET, end='')
        print(Fore.RED + "|" * self.red_count + Fore.RESET, end='')
        print(Fore.YELLOW + "|" * self.yellow_count + Fore.RESET, end='')
        print(Fore.GREEN + "|" * self.green_count + Fore.RESET, end='')
        print(Fore.CYAN + "|" * self.cyan_count + Fore.RESET)

        if not self.difficulty == 1:
            print(Fore.CYAN + " " * self.cyan_count + Fore.RESET, end='')
            print(Fore.GREEN + "|" * self.green_count + Fore.RESET, end='')
            print(Fore.YELLOW + "|" * self.yellow_count + Fore.RESET, end='')
            print(Fore.RED + "|" * self.red_count + Fore.RESET, end='')
            print(Fore.YELLOW + "|" * self.yellow_count + Fore.RESET, end='')
            print(Fore.GREEN + "|" * self.green_count + Fore.RESET, end='')
            print(Fore.CYAN + " " * self.cyan_count + Fore.RESET)

        print(Fore.CYAN + " " * self.cyan_count + Fore.RESET, end='')
        print(Fore.GREEN + " " * self.green_count + Fore.RESET, end='')
        print(Fore.YELLOW + "|" * self.yellow_count + Fore.RESET, end='')
        print(Fore.RED + "|" * self.red_count + Fore.RESET, end='')
        print(Fore.YELLOW + "|" * self.yellow_count + Fore.RESET, end='')
        print(Fore.GREEN + " " * self.green_count + Fore.RESET, end='')
        print(Fore.CYAN + " " * self.cyan_count + Fore.RESET, )

        print(Fore.CYAN + " " * self.cyan_count + Fore.RESET, end='')
        print(Fore.GREEN + " " * self.green_count + Fore.RESET, end='')
        print(Fore.YELLOW + " " * self.yellow_count + Fore.RESET, end='')
        print(Fore.RED + "|" * self.red_count + Fore.RESET, end='')
        print(Fore.YELLOW + " " * self.yellow_count + Fore.RESET, end='')
        print(Fore.GREEN + " " * self.green_count + Fore.RESET, end='')
        print(Fore.CYAN + " " * self.cyan_count + Fore.RESET, )

    def __start_game(self):
        """Private method: for playing"""
        # Keep moving while the user doesn't press enter button
        while self.finish_game is None:
            # If the direction is from the left to the right, move forward otherwise move backward
            if self.direction:
                self.__move_forward()
            else:
                self.__move_backward()

    def __move_forward(self):
        """Private method: for moving the arrow forward, it uses the __move() method to move"""
        self.__move()
        # Keep incrementing the position until it reaches the end
        self.position += 1
        # When the position of the arrow reaches the end, change the direction
        if self.position == self.maximum:
            self.direction = False

    def __move_backward(self):
        """Private method: for moving the arrow backward, it uses the __move() method to move"""
        self.__move()
        # Keep decrementing the position until it reaches the beginning
        self.position -= 1
        # When the position of the arrow reaches the beginning, change the direction
        if self.position == 1:
            self.direction = True

    def __move(self):
        """Private method: for moving the arrow"""
        # Clear the row
        print("\b" * self.maximum, end='')
        # print multiple spaces (position - 1 spaces) and then print the arrow ^
        print(' ' * (self.position - 1), Fore.WHITE + "^" + Fore.RESET, sep='', end='')
        # Wait a certain time between each movement
        sleep(self.sleep_time)

    def __show_result(self):
        """Private method: for showing the final result"""
        # calculate level-score
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

        # clear the screen
        print("\b" * self.maximum, end='')

        # calculate the extra slashes in the level
        # self.maximum // 2 == the center
        # abs(self.maximum // 2 - self.position) == the difference between the center and
        # the position of the arrow
        extra = (self.maximum // 2 - abs(self.maximum // 2 - self.position))

        # calculate the final score and print it
        self.total = self.score + extra
        art_text = text2art(str(self.total), font='Fraktur')  # Banner3-D, Larry 3D, Fraktur
        print(Fore.WHITE, art_text, Fore.RESET)

        # play sounds
        if self.total > self.high:
            winsound.PlaySound('win.wav', winsound.SND_FILENAME)
        elif self.total > self.low:
            winsound.PlaySound('mid.wav', winsound.SND_FILENAME)
        else:
            winsound.PlaySound('lose.wav', winsound.SND_FILENAME)


def main():
    # dictionary for storing players names, and scores
    players = dict()
    # list for sorting the players according to their scores
    players_list = list()
    # loop check variable
    still_playing = '1'
    while still_playing == '1':
        g = Game()
        name, total = g.play_game()
        players[name] = total
        still_playing = input(
            Fore.BLUE + f'\nEnter {Fore.BLACK}(1){Fore.BLUE} to play again, and press enter to exit...  '
            + Fore.RESET)

    # sort the players according to their scores
    for name, total in players.items():
        new_player = (total, name)
        players_list.append(new_player)
    players_list = sorted(players_list, reverse=True)

    art_text = text2art("\nBest results: ", "fancy12")
    print(Fore.WHITE + art_text + Fore.RESET)
    for total, name in players_list:
        print(Fore.WHITE + f"\n{name}: {Fore.BLACK}{total}" + Fore.RESET)


# It won't work if the user import my module
if __name__ == '__main__':
    main()
