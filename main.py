import os
from threading import Thread

from utilities.terminal_colors import *
from utilities.mover import Mover
from utilities.printer import Printer


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
        self.level = 1
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
        # high level score
        self.high = 400
        # mid level score
        self.mid = 300
        # low level score
        self.low = 200

    def play_game(self):
        """Public method: for starting the game"""

        # For supporting windows system colors
        os.system("color")

        # For inserting the name of the player and the level of the game
        self.__insert_user_data()

        # determine how fast should the arrow be according to the level of the game
        self.__specify_arrow_speed()

        # Start drawing the goal
        Printer.print_goal(self)

        # Thread for moving the arrow
        t = Thread(target=self.__start_game)
        t.start()

        # The main thread is waiting for an input from the user
        self.finish_game = input('')

        # After pressing the enter button, Printer.print_result(self) method will be invoked
        Printer.print_result(self)

        # After completing one game, it will return the name, the level, and the result of the player
        return self.name, self.total, self.level

    def __insert_user_data(self):
        """Private method: for getting user data"""

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
                Fore.YELLOW + '\nWrong, The level should be 1, 2, or 3, try again > ' + Fore.RESET)
        self.level = int(user_input)

    def __specify_arrow_speed(self):
        """Private method: for changing arrow speed"""

        # Change the duration according to the level of the game
        if self.level == 1:
            self.sleep_time = 0.03
        elif self.level == 2:
            self.sleep_time = 0.02
        else:
            self.sleep_time = 0.01

    def __start_game(self):
        """Private method: for playing"""

        # Keep moving while the user doesn't press enter button
        while self.finish_game is None:
            # If the direction is from the left to the right, move forward otherwise move backward
            if self.direction:
                Mover.move_forward(self)
            else:
                Mover.move_backward(self)


def main():
    while True:
        option = input(Fore.WHITE + """
    1) play (multi players)
    2) play (against the computer)
    3) show the history
    4) quit
    > """ + Fore.RESET)
        while not (option == "1" or option == "2" or option == "3" or option == "4"):
            option = input(Fore.YELLOW + """
    Wrong, you should enter the number of below options
    1) play (multi players)
    2) play (against the computer)
    3) show the history
    4) quit
    > """ + Fore.RESET)
        if option == "1":
            # dictionary for storing players names, and scores
            players = dict()
            # list for sorting the players according to their scores
            players_list = list()
            # loop check variable
            still_playing = '1'
            while still_playing == '1':
                g = Game()
                name, total, difficulty = g.play_game()
                players[name] = [total, difficulty]
                still_playing = input(
                    Fore.BLUE + f'\nEnter {Fore.BLACK}(1){Fore.BLUE} to play again, and press enter to exit...  '
                    + Fore.RESET)

            # print the recently history
            Printer.print_history(players, players_list)
        elif option == "2":
            print("Under maintenance :)")
        elif option == "3":
            Printer.print_whole_history()
        else:
            quit()


# It won't work if the user import my module
if __name__ == '__main__':
    main()
