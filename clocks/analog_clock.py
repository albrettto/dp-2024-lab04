from interfaces import BaseAnalogClock
from consts import DayNightDivision


class AnalogClock(BaseAnalogClock):
    def __init__(self):
        self.year = 1
        self.month = 1
        self.day = 1
        self.hour_angle = 0.0
        self.minute_angle = 0.0
        self.second_angle = 0.0
        self.day_night_division = DayNightDivision.AM

    def set_date_time(
        self,
        year: int,
        month: int,
        day: int,
        hour_angle: float,
        minute_angle: float,
        second_angle: float,
        day_night_division: DayNightDivision,
    ):
        self.year = year
        self.month = month
        self.day = day
        self.hour_angle = hour_angle
        self.minute_angle = minute_angle
        self.second_angle = second_angle
        self.day_night_division = day_night_division

    def get_hour_angle(self) -> float:
        return self.hour_angle

    def get_minute_angle(self) -> float:
        return self.minute_angle

    def get_second_angle(self) -> float:
        return self.second_angle

    def get_year(self) -> int:
        return self.year

    def get_month(self) -> int:
        return self.month

    def get_day(self) -> int:
        return self.day

    def get_day_night_division(self) -> DayNightDivision:
        return self.day_night_division
