class SmartHouse:

    def __init__(self, temperature_pm: int, is_light_on: bool):
        self.temperatur = temperature_pm
        self.is_light_on = is_light_on

    def increase_temperature(self):
        if self.temperatur < 40:
            self.temperatur += 1
    def decrease_temperature(self):
        if self.temperatur > 0:
            self.temperatur -= 1
dom = SmartHouse(temperature_pm=20, is_light_on=True)



