from observer.Displays import CurrentConditionsDisplay, StatisticsDisplay, ForecastDisplay
from observer.weatherData import WeatherData

if __name__ == "__main__":
    w_data = WeatherData()

    current_display = CurrentConditionsDisplay(w_data)
    statistic_display = StatisticsDisplay(w_data)
    forcast_display = ForecastDisplay(w_data)

    w_data.set_measurements(80, 65, 30.4)
    w_data.set_measurements(82, 70, 29.2)
    w_data.set_measurements(78, 90, 29.2)