from Duck import Duck
from MallardDuck import MallardDuck
from FlyNoWay import FlyNoWay 

myDuck = MallardDuck()

myDuck.performFly()

print "I'm changing Behavior now!"

myDuck.setBehavior(FlyNoWay)

myDuck.performFly()

