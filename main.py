from threading import Thread
from time import sleep
import os
from termcolor import colored


class Game:
    def __init__(self):
        self.name = ''
        self.direction = True
        self.sleep_time = 0.03
        # Maximum number of slashes
        self.maximum = 150
        self.result = None
        self.position = 1
        self.difficulty = 1
        # Number of cyan slashes
        self.cyan_count = 0
        # Number of green slashes
        self.green_count = 0
        # Number of yellow slashes
        self.yellow_count = 0
        # Number of red slashes
        self.red_count = 0
        self.total = 0

    def play_game(self):
        """Public method: for starting the game"""
        try:
            os.system("color")
            self.name = input(colored('\nEnter your name > ', 'yellow'))
            self.difficulty = int(input(colored('\nEnter the level > ', "white")))
            if self.difficulty == 1:
                self.sleep_time = 0.03
            elif self.difficulty == 2:
                self.sleep_time = 0.02
            else:
                self.sleep_time = 0.01
            print("""
Press enter to stop...
                  """)
            self.__draw_goal()
            # Thread for moving the arrow
            t = Thread(target=self.__start_game)
            t.start()
            # The main thread is waiting for an input from the user
            self.result = input('')
            # After pressing the enter button, __show_result() method will be invoked
            self.__show_result()
            # After completing one game, it will return the name and the result of the player
            return self.name, self.total
        except ValueError:
            print(colored("Wrong Input type, make sure that you enter an integer value!", "red"))

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

        print(colored("|" * self.cyan_count, "cyan"), end='')
        print(colored("|" * self.green_count, "green"), end='')
        print(colored("|" * self.yellow_count, "yellow"), end='')
        print(colored("|" * self.red_count, "red"), end='')
        print(colored("|" * self.yellow_count, "yellow"), end='')
        print(colored("|" * self.green_count, "green"), end='')
        print(colored("|" * self.cyan_count, "cyan"))

        if not self.difficulty == 1:
            print(colored(" " * self.cyan_count, "cyan"), end='')
            print(colored("|" * self.green_count, "green"), end='')
            print(colored("|" * self.yellow_count, "yellow"), end='')
            print(colored("|" * self.red_count, "red"), end='')
            print(colored("|" * self.yellow_count, "yellow"), end='')
            print(colored("|" * self.green_count, "green"), end='')
            print(colored(" " * self.cyan_count, "cyan"))

        print(colored(" " * self.cyan_count, "cyan"), end='')
        print(colored(" " * self.green_count, "green"), end='')
        print(colored("|" * self.yellow_count, "yellow"), end='')
        print(colored("|" * self.red_count, "red"), end='')
        print(colored("|" * self.yellow_count, "yellow"), end='')
        print(colored(" " * self.green_count, "green"), end='')
        print(colored(" " * self.cyan_count, "cyan"))

        print(colored(" " * self.cyan_count, "cyan"), end='')
        print(colored(" " * self.green_count, "green"), end='')
        print(colored(" " * self.yellow_count, "yellow"), end='')
        print(colored("|" * self.red_count, "red"), end='')
        print(colored(" " * self.yellow_count, "yellow"), end='')
        print(colored(" " * self.green_count, "green"), end='')
        print(colored(" " * self.cyan_count, "cyan"))

    def __start_game(self):
        """Private method: for playing"""
        # While the user doesn't press enter button
        while self.result is None:
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
        print(' ' * (self.position - 1), colored("^", "magenta"), sep='', end='')
        # Wait a certain time between each movement
        sleep(self.sleep_time)

    def __show_result(self):
        """Private method: for showing the final result"""
        # calculate level score
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
        print(colored('Your score is ' + str(self.total),
                      'blue'))


def main():
    # dictionary for storing players names, and scores
    players = dict()
    # list for sorting the players according to their scores
    players_list = list()
    # loop check variable
    still_playing = '1'
    try:
        while still_playing == '1':
            g = Game()
            name, total = g.play_game()
            players[name] = total
            still_playing = input(colored('Enter 1 to play again, and press enter to exit...  ', 'green'))
    except ValueError:
        print(colored("Wrong Input type, make sure that you enter an integer value!", "red"))

    # sort the players according to their scores
    for name, total in players.items():
        new_player = (total, name)
        players_list.append(new_player)
    players_list = sorted(players_list, reverse=True)

    print(colored('Best results: ', 'yellow'))
    for total, name in players_list:
        print(colored(f"{name}: {total}", "blue"))


# It won't work if the user import my module
if __name__ == '__main__':
    main()
