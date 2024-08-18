class Cube:
    SIDES_COUNT = 12

    def __init__(self, filled, r, g, b, *args):
        new_args = []
        x = 1
        if len(args) == self.SIDES_COUNT:
            for i in args:
                n = args[x]
                if i == n:
                    new_args.append(i)
                    if x < (len(args) - 1):
                        x += 1
                    self.__sides = new_args
                else:
                    self.__sides = [self.SIDES_COUNT] * self.SIDES_COUNT
                    break
        else:
            self.__sides = [self.SIDES_COUNT] * self.SIDES_COUNT

    def get_sides(self):
        return self.__sides


cu4 = Cube(0, 55, 66, 188, 55, 5, 55, 55, 55, 55, 10, 55, 55, 55, 55, 55)
print(cu4.get_sides())
cu3 = Cube(0, 55, 66, 188, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55)
print(cu3.get_sides())