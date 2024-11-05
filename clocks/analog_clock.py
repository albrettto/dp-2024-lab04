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
        """
        Устанавливает текущую дату

        :param year: год
        :param month: месяц
        :param day: день
        :param hour_angle: угол стрелки часов
        :param minute_angle: угол минутной стрелки
        :param second_angle: угол секундной стрелки
        :param day_night_division: текущее время суток (день / ночь)
        """
        self.year = year
        self.month = month
        self.day = day
        self.hour_angle = hour_angle
        self.minute_angle = minute_angle
        self.second_angle = second_angle
        self.day_night_division = day_night_division

    def get_hour_angle(self) -> float:
        """
        Возвращает текущий угол стрелки часов
        """
        return self.hour_angle

    def get_minute_angle(self) -> float:
        """
        Возвращает текущий угол минутной стрелки
        """
        return self.minute_angle

    def get_second_angle(self) -> float:
        """
        Возвращает текущий угол секундной стрелки
        """
        return self.second_angle

    def get_year(self) -> int:
        """
        Возвращает текущий год (от установленного пользователем)
        """
        return self.year

    def get_month(self) -> int:
        """
        Возвращает текущий месяц (от установленного пользователем)
        """
        return self.month

    def get_day(self) -> int:
        """
        Возвращает текущий день (от установленного пользователем)
        """
        return self.day

    def get_day_night_division(self) -> DayNightDivision:
        """
        Возвращает текущее время суток (день / ночь)
        """
        return self.day_night_division
