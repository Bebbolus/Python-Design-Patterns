from WaetherData import WaetherData
from CurrentConditionDisplay import CurrentConditionDisplay

wd = WaetherData()

cd  = CurrentConditionDisplay(wd)

wd.setMeasurements(20,75,30)


