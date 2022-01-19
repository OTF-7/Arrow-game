from utilities.terminal_colors import *
from time import sleep


class Mover:
    @staticmethod
    def move_forward(self):
        """public method: for moving the arrow forward, it uses the __move() method to move"""

        Mover.__move(self)

        # Keep incrementing the position until it reaches the end
        self.position += 1

        # When the position of the arrow reaches the end, change the direction
        if self.position == self.maximum:
            self.direction = False

    @staticmethod
    def move_backward(self):
        """Public method: for moving the arrow backward, it uses the __move() method to move"""

        Mover.__move(self)

        # Keep decrementing the position until it reaches the beginning
        self.position -= 1

        # When the position of the arrow reaches the beginning, change the direction
        if self.position == 1:
            self.direction = True

    @staticmethod
    def __move(self):
        """Private method: for moving the arrow"""

        # Clear the row
        print("\b" * self.maximum, end='')

        # print multiple spaces (position - 1 spaces) and then print the arrow ^
        print(' ' * (self.position - 1), Fore.WHITE + "^" + Fore.RESET, sep='', end='')

        # Wait a certain time between each movement
        sleep(self.sleep_time)
