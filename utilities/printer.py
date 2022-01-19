from utilities.terminal_colors import *
import winsound
from art import *


class Printer:
    @staticmethod
    def print_menu():
        pass

    @staticmethod
    def print_goal(self):
        """Public method: for drawing the goal"""

        print(Fore.BLUE + """
        Press enter to stop...
                      """ + Fore.RESET)

        # specify the number of slashes in each level
        if self.level == 1:
            self.cyan_count = 0
            self.green_count = 40
            self.yellow_count = 25
            self.red_count = 20
        elif self.level == 2:
            self.cyan_count = 25
            self.green_count = 25
            self.yellow_count = 15
            self.red_count = 20
        else:
            self.cyan_count = 30
            self.green_count = 25
            self.yellow_count = 15
            self.red_count = 10

        # print the numbers and the points
        Printer.__print_points_numbers()

        # print the goal slashes
        Printer.__print_slashes(self)

    @staticmethod
    def __print_points_numbers():
        # for printing the points' numbers
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

    @staticmethod
    def __print_slashes(self):
        print(Fore.CYAN + "|" * self.cyan_count + Fore.RESET, end='')
        print(Fore.GREEN + "|" * self.green_count + Fore.RESET, end='')
        print(Fore.YELLOW + "|" * self.yellow_count + Fore.RESET, end='')
        print(Fore.RED + "|" * self.red_count + Fore.RESET, end='')
        print(Fore.YELLOW + "|" * self.yellow_count + Fore.RESET, end='')
        print(Fore.GREEN + "|" * self.green_count + Fore.RESET, end='')
        print(Fore.CYAN + "|" * self.cyan_count + Fore.RESET)

        if not self.level == 1:
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

    @staticmethod
    def print_result(self):
        # calculate level-score
        if self.level == 1:
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
        color = Fore.RED if self.score == self.high or self.level == 1 and self.score == self.mid else \
            Fore.YELLOW if self.score == self.mid or self.level == 1 and self.score == self.low else \
                Fore.GREEN if self.score == self.low or self.level == 1 \
                    else Fore.CYAN
        art_text = text2art(str(self.total), font='Fraktur')
        print(color, art_text, Fore.RESET)

        # for playing sounds
        Printer.__play_sounds(self)

    @staticmethod
    def __play_sounds(self):
        # check the level and the score
        if self.score == self.high or self.level == 1 and self.score == self.mid:
            winsound.PlaySound('sounds/win.wav', winsound.SND_FILENAME)
        elif self.score > self.low or self.level == 1 and self.score == self.low:
            winsound.PlaySound('sounds/mid.wav', winsound.SND_FILENAME)
        else:
            winsound.PlaySound('sounds/lose.wav', winsound.SND_FILENAME)

    @staticmethod
    def print_history(players, players_list):
        """public method: for printing the recently history"""

        # sort the players according to their scores
        for name, data in players.items():
            new_player = (data, name)
            players_list.append(new_player)
        players_list = sorted(players_list, reverse=True)
        with open("utilities/history.txt", 'a') as file:
            art_text = text2art("\nBest results: ", "fancy12")
            print(Fore.WHITE + art_text + Fore.RESET)
            print('''-----------------------------------------
                                (level 1)                 ''')
            for data, name in players_list:
                if data[1] == 1:
                    print(Fore.WHITE + f"   \n{name}: {Fore.BLACK}{list(data)[0]}" + Fore.RESET)
                    file.write(f"{name}:{data[0]}:{data[1]}\n")

            print('''-----------------------------------------
                                (level 2)                 ''')
            for data, name in players_list:
                if data[1] == 2:
                    print(Fore.WHITE + f"   \n{name}: {Fore.BLACK}{list(data)[0]}" + Fore.RESET)
                    file.write(f"{name}:{data[0]}:{data[1]}\n")

            print('''-----------------------------------------
                                (level 3)                 ''')
            for data, name in players_list:
                if data[1] == 3:
                    print(Fore.WHITE + f"   \n{name}: {Fore.BLACK}{list(data)[0]}" + Fore.RESET)
                    file.write(f"{name}:{data[0]}:{data[1]}\n")

    @staticmethod
    def print_whole_history():
        level1_list, level2_list, level3_list = list(), list(), list()
        with open("utilities/history.txt") as file:
            for line in file.readlines():
                line = line.rstrip("\n")
                name, total, level = line.split(":")
                if level == "1":
                    level1_list.append((total, name))
                elif level == "2":
                    level2_list.append((total, name))
                else:
                    level3_list.append((total, name))

            art_text = text2art("\nBest results: ", "fancy12")
            print(Fore.WHITE + art_text + Fore.RESET)

            print(level1_list)
            print(level2_list)
            print(level3_list)
            print('''-----------------------------------------
                                (level 1)                 ''')
            for (total, name) in level1_list:
                print(Fore.WHITE + f"   \n{name}: {Fore.BLACK}{total}" + Fore.RESET)

            print('''-----------------------------------------
                                (level 2)                 ''')
            for (total, name) in level2_list:
                print(Fore.WHITE + f"   \n{name}: {Fore.BLACK}{total}" + Fore.RESET)

            print('''-----------------------------------------
                                (level 3)                 ''')
            for (total, name) in level3_list:
                print(Fore.WHITE + f"   \n{name}: {Fore.BLACK}{total}" + Fore.RESET)
