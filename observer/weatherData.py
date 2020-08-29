from abc import abstractmethod, ABC


class Observer:
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        pass

class Subject(ABC):
    @abstractmethod
    def registerObserver(self, o: Observer) -> None:
        pass

    @abstractmethod
    def removeObserver(self, o: Observer) -> None:
        pass

    @abstractmethod
    def notifyObservers(self) -> None:
        pass

class DisplayElement:
    @abstractmethod
    def display(self) -> None :
        pass

class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0.0
        self.pressure = 0.0

    def registerObserver(self, observer) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def removeObserver(self, observer) -> None:
        try:
            self.observers.remove(observer)
        except ValueError:
            print("{} doesn't belong to the list of observers.".format(observer))

    def notifyObservers(self) -> None:
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notifyObservers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()




