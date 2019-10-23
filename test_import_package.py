
class Cat(object):
    """这是一个猫类"""

    def __init__(self, name='doudou', weight=5):
        self.name = name
        self.weight = weight
        self.__age = 5

    def eat_fish(self):
        print("%s 爱吃鱼" % self.name)

    def get_weight(self):
        print("%s 的体重是 %.3f千克" % (self.name, self.weight))


tom = Cat(weight=10, name='豆豆')
tom.eat_fish()
tom.get_weight()
