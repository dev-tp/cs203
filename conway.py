from random import randint
from time import sleep
from os import name, system


class Field(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[False for i in range(width)] for j in range(height)]

    def set(self, x, y, value):
        self.grid[y][x] = value

    def alive(self, x, y):
        x += self.width
        x %= self.width
        y += self.height
        y %= self.height
        return self.grid[y][x]

    def next(self, x, y):
        alive = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (j != 0 or i != 0) and self.alive(x + i, y + j):
                    alive += 1
        return alive == 3 or alive == 2 and self.alive(x, y)


class Life(object):
    def __init__(self, width, height):
        self.first_field = Field(width, height)
        self.second_field = Field(width, height)
        self.width = width
        self.height = height

        for _ in range(width * height / 4):
            self.first_field.set(randint(0, width - 1), randint(0, height - 1), True)

    def step(self):
        for y in range(self.height):
            for x in range(self.width):
                self.second_field.set(x, y, self.first_field.next(x, y))
        self.first_field, self.second_field = self.second_field, self.first_field

    def __str__(self):
        result = ""
        for y in range(self.height):
            for x in range(self.width):
                result = result + ('*' if self.first_field.alive(x, y) else ' ')
            result = result + "\n"
        return result


def main():
    clear = "clear" if name != "nt" else "cls"
    life = Life(40, 15)

    for _ in range(50):
        life.step()
        system(clear)
        print life
        sleep(0.21)


if __name__ == "__main__":
    main()