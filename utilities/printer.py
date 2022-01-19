from utilities.terminal_colors import *


class Printer:
    @staticmethod
    def print_goal():
        pass

    @staticmethod
    def print_result():
        pass

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
