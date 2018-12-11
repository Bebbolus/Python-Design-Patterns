from DisplayElement import DisplayElement
from Subject import Subject

class CurrentConditionDisplay( DisplayElement):
    def __init__(self, sub):
        self.temperature =0
        self.humidity=0
        assert isinstance( sub, Subject)
        sub.registerObserver( self )

    def display( self ):
        print("Current Conditions:")
        print("\n>>Temperature = {}\n>>Humidity = {}".format(self.temperature, self.humidity))
    
    def update( self, temp, humi, press):
        self.temperature = temp
        self.humidity = humi

        self.display()
