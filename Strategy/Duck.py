from FlyBehavior import FlyBehavior

class Duck(object):
    def __init__(self, flyBehavior, quackBehavior):
        self.setBehavior(flyBehavior)

    def performFly(self):
        f = self.flyBehavior()
        f.fly()

    def setBehavior(self, behavior):
        assert issubclass(behavior, FlyBehavior)
        self.flyBehavior = behavior
        
