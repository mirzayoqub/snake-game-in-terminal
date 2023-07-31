import random
class snake:
    def __init__(self):
        self.width = 14
        self.height = 14
        self.x = self.width//2
        self.y = self.height//2
        self.snake_list = [(self.x, self.y)]
        self.eat = self._eat_random_()

    def __print_dash__(self):
        for x in range(self.width):
            for y in range(self.height):
                if x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1:
                    print("#", end='  ')
                elif (x, y) in [(i[0], i[1]) for i in self.snake_list]:
                    print('@', end='  ')
                elif (x, y) == self.eat:
                    print('*', end='  ')
                else:
                    print(' ', end='  ')
            print('\n', end='')

    def _eat_random_(self):
        return (random.randint(1, self.width-2), random.randint(1, self.height-2))


    def snake_len(self, arg):
        if arg == 8:
            self.x -= 1
        elif arg == 2:
            self.x += 1
        elif arg == 4:
            self.y -= 1
        elif arg == 6:
            self.y += 1
        else:
            print("Please enter from 8, 4, 6, 2\n\n\n")


        if self.eat != (self.x, self.y):
            self.snake_list.pop()
            self.snake_list.insert(0, (self.x, self.y))
        else:
            self.snake_list.insert(0,(self.x, self.y))
            self.eat = self._eat_random_()


    def play_game(self):
        while True:
            self.__print_dash__()
            arg = int(input("Enter number arove 8, 4, 6, 2:  "))
            self.snake_len(arg)


if __name__ == '__main__':
    Snake_game = snake()
    Snake_game.play_game()
