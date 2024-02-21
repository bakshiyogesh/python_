class Battery:
    def battery_info(self):
        return "Battery Life info."

class Engine:
    def engine_info(self):
        return "Engine is saved."

class EngineBattery(Battery,Engine):
    pass
print(EngineBattery)
