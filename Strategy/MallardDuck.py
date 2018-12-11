from Duck import Duck
from FlyWithWings import FlyWithWings


class MallardDuck(Duck):
     def __init__(self):
        super(MallardDuck, self).__init__(FlyWithWings, "gigi")


