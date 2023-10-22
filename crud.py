"""CRUD operations"""

from model import db, User, PickleballData


def create_user(first_name):
    """Create and return a new user"""

    user = User(first_name=first_name)
    return user


def create_workout(startDate, endDate, activityType, duration, HKWeatherHumidity, totalEnergyBurned, HKWeatherTemperature):
    # data = PickleballData(startDate=startDate,
    #                       endDate=endDate, activityType=activityType)
    data = PickleballData(startDate=startDate, endDate=endDate, activityType=activityType, duration=duration,
                          HKWeatherHumidity=HKWeatherHumidity, totalEnergyBurned=totalEnergyBurned,
                          HKWeatherTemperature=HKWeatherTemperature)
    return data
