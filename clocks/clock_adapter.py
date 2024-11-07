from clocks.analog_clock import AnalogClock
from clocks.time_converter import TimeConverter
from consts import DayNightDivision
from interfaces import BaseDigitalClock
from consts.time_consts import TimeConsts
from datetime import datetime


class ClockAdapter(BaseDigitalClock):
    """
    Адаптер для преобразования аналоговых часов в цифровые.
    """

    def __init__(self, analog_clock: AnalogClock):
        """
        Инициализирует адаптер для работы с аналоговыми часами.

        :param analog_clock: экземпляр аналоговых часов
        """
        self._analog_clock = analog_clock

    def set_date_time(self, date: datetime) -> None:
        """
        Задает текущую дату

        :param date: дата в формате datetime
        """
        year = date.year
        month = date.month
        day = date.day
        hour_angle = TimeConverter.hour_to_angle(date.hour, date.minute)
        minute_angle = TimeConverter.minute_to_angle(date.minute, date.second)
        second_angle = date.second * TimeConsts.DEG_FOR_SEC
        day_night_division = (
            DayNightDivision.AM
            if TimeConsts.MIDNIGHT <= date.hour < TimeConsts.MIDDAY
            else DayNightDivision.PM
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
        hour = TimeConverter.angle_to_hour(
            self._analog_clock.get_hour_angle(), day_night_division
        )
        minute = TimeConverter.angle_to_minute(self._analog_clock.get_minute_angle())
        second = int(self._analog_clock.get_second_angle() / TimeConsts.DEG_FOR_SEC)
        return datetime(year, month, day, hour, minute, second)
