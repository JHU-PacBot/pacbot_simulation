from variables import *
from grid import *

class PacBot:

    """
        Allows initializing and updating information about PacBot
    """
    def __init__(self):
        self.respawn()

    def respawn(self):
        self.pos = pacbot_starting_pos
        self.direction = pacbot_starting_dir

    def update(self, position):
        if position[0] > self.pos[0]:
            self.direction = right
        elif position[0] < self.pos[0]:
            self.direction = left
        elif position[1] > self.pos[1]:
            self.direction = up
        elif position[1] < self.pos[1]:
            self.direction = down
        self.pos = position

# algorithm to make pac-man move
    def move(self, game_state):
        save = self.pos
        if self.direction == left:
            self.pos = (self.pos[0] - 1, self.pos[1])
        elif self.direction == right:
            self.pos = (self.pos[0] + 1, self.pos[1])
        elif self.direction == up:
            self.pos = (self.pos[0], self.pos[1] + 1)
        else:
            self.pos = (self.pos[0], self.pos[1] - 1)

        if grid[self.pos[0]][self.pos[1]] == I or grid[self.pos[0]][self.pos[1]] == n:
            self.pos = save

