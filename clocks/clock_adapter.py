from clocks.analog_clock import AnalogClock
from consts import DayNightDivision
from interfaces import BaseDigitalClock
from datetime import datetime


class ClockAdapter(BaseDigitalClock):
    """
    Константное число для обозначения кол-ва часов в дне
    _HOURS (int): 12

    Константное число для обозначения кол-ва минут (секунд) в часе (минуте)
    _MIN_OR_SEC (int): 60

    Часовая стрелка совершает полный оборот (360°) за 12 часов,
    поэтому каждое значение часа эквивалентно 30° (360° / 12).
    _DEG_FOR_HOUR (int): 30°

    Минутная и секундная стрелки совершают полный оборот (360°) за 60 минут(секунд),
    поэтому каждое значение минуты(секунды) эквивалентно 6° (360° / 60).
    _DEG_FOR_MIN_OR_SEC (int): 6°

    """
    _HOURS = 12
    _MIN_OR_SEC = 60
    _DEG_FOR_HOUR = 30
    _DEG_FOR_MIN_OR_SEC = 6

    def __init__(self, analog_clock: AnalogClock):
        self._analog_clock = analog_clock

    def _hour_to_angle(self, hour: int, minute: int) -> float:
        """
        Преобразует время в часах и минутах в угол для часовой стрелки на аналоговых часах.
        Метод также учитывает сдвиг часовой стрелки за счет минут.

        Args:
            hour (int): Часы (от 0 до 23).
            minute (int): Минуты (от 0 до 59).

        Returns:
            float: Угол в градусах для часовой стрелки.
        """
        return hour % self._HOURS * self._DEG_FOR_HOUR + minute / self._MIN_OR_SEC * self._DEG_FOR_HOUR

    def _minute_to_angle(self, minute: int, second: int) -> float:
        """
        Преобразует время в минутах и секундах в угол для минутной стрелки на аналоговых часах.
        Метод также учитывает сдвиг минутной стрелки за счет секунд.

        Args:
            minute (int): Минуты (от 0 до 59).
            second (int): Секунды (от 0 до 59).

        Returns:
            float: Угол в градусах для минутной стрелки.
        """
        return minute * self._DEG_FOR_MIN_OR_SEC + second / self._MIN_OR_SEC * self._DEG_FOR_MIN_OR_SEC

    def _angle_to_hour(self, hour_angle: float, day_night_division: DayNightDivision) -> int:
        """
        Преобразует угол часовой стрелки обратно в часы.

        Args:
            hour_angle (float): Угол в градусах для часовой стрелки.
            day_night_division (DayNightDivision): Текущее время суток: AM - день; PM - вечер.

        Returns:
            int: Число часов (от 0 до 23).
        """
        hour = int(hour_angle / self._DEG_FOR_HOUR)
        if day_night_division == DayNightDivision.PM and hour != 12:
            hour += 12
        elif day_night_division == DayNightDivision.AM and hour == 12:
            hour = 0
        return hour

    def _angle_to_minute(self, minute_angle: float) -> int:
        """
        Преобразует угол минутной стрелки обратно в минуты.

        Args:
            minute_angle (float): Угол в градусах для минутной стрелки.

        Returns:
            int: Число минут (от 0 до 59).
        """
        return int(minute_angle / self._DEG_FOR_MIN_OR_SEC)


    def set_date_time(self, date: datetime) -> None:
        """
        Задает текущую дату

        :param date: дата в формате datetime
        """
        year = date.year
        month = date.month
        day = date.day
        hour_angle = self._hour_to_angle(date.hour, date.minute)
        minute_angle = self._minute_to_angle(date.minute, date.second)
        second_angle = date.second * self._DEG_FOR_MIN_OR_SEC
        day_night_division = (
            DayNightDivision.AM if 0 <= date.hour < 12 else DayNightDivision.PM
        )
        self._analog_clock.set_date_time(
            year, month, day, hour_angle, minute_angle, second_angle, day_night_division
        )

    def get_date_time(self) -> datetime:
        """
        Возвращает текущую дату в формате datetime
        """
        year = self._analog_clock.get_year()
        month = self._analog_clock.get_month()
        day = self._analog_clock.get_day()
        day_night_division = self._analog_clock.get_day_night_division()
        hour = self._angle_to_hour(self._analog_clock.get_hour_angle(), day_night_division)
        minute = self._angle_to_minute(self._analog_clock.get_minute_angle())
        second = int(self._analog_clock.get_second_angle() / self._DEG_FOR_MIN_OR_SEC)
        return datetime(year, month, day, hour, minute, second)
