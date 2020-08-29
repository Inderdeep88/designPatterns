from observer.weatherData import Observer, DisplayElement, Subject


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: Subject):
        self.temperature = 0
        self.humidity = 0
        self.weather_data = weather_data
        self.weather_data.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self) -> None:
        print("Current conditions: Temp -", self.temperature,"F and Humidity -", self.humidity)


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: Subject):
        self.maxTemp = 0
        self.minTemp = 500
        self.tempSum = 0
        self.numReadings = 0
        self.weather_data = weather_data
        self.weather_data.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self.tempSum += temp
        self.numReadings = self.numReadings + 1

        if (temp > self.maxTemp):
            self.maxTemp = temp

        if (temp < self.minTemp):
            self.minTemp = temp

        self.display()

    def display(self) -> None:
        print("Avg/Max/Min temperature = ",(self.tempSum/self.numReadings), "/", self.maxTemp, "/", self.minTemp)


class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: Subject):
        self.currentPressure = 29.92
        self.lastPressure = 0
        self.weather_data = weather_data
        self.weather_data.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self.lastPressure = self.currentPressure
        self.currentPressure = pressure

        self.display()

    def display(self) -> None:
        if (self.currentPressure > self.lastPressure):
            print("Forecast: Improving weather on the way!")
        elif (self.currentPressure == self.lastPressure):
            print("Forecast: More of the same")
        elif (self.currentPressure < self.lastPressure):
            print("Forecast: Watch out for cooler, rainy weather")
