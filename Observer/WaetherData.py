from Subject import Subject
from Observer import Observer

class WaetherData( Subject ):
    def __init__( self ):
        self.observers = []
        self.humidity = 0
        self.temperature = 0
        self.pressure = 0

    
    def registerObserver( self, obs ):
        assert isinstance(obs, Observer)
        self.observers.append(obs)

    def removeObserver( self, obs ):
        self.observer.remove(obs)

    def notifyObserver( self ):
        for obs in self.observers:
            obs.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged( self ):
        self.notifyObserver()

    def setMeasurements( self, temp, humi, press):
        self.temperature = temp
        self.humidity = humi
        self.pressure = press

        self.measurementsChanged()
        
