from abc import ABC, abstractmethod
from consts import DayNightDivision


class BaseAnalogClock(ABC):
    @abstractmethod
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
        raise NotImplementedError()

    @abstractmethod
    def get_hour_angle(self) -> float:
        """
        Возвращает текущий угол стрелки часов
        """
        raise NotImplementedError()

    @abstractmethod
    def get_minute_angle(self) -> float:
        """
        Возвращает текущий угол минутной стрелки
        """
        raise NotImplementedError()

    @abstractmethod
    def get_second_angle(self) -> float:
        """
        Возвращает текущий угол секундной стрелки
        """
        raise NotImplementedError()

    @abstractmethod
    def get_year(self) -> int:
        """
        Возвращает текущий год (от установленного пользователем)
        """
        raise NotImplementedError()

    @abstractmethod
    def get_month(self) -> int:
        """
        Возвращает текущий месяц (от установленного пользователем)
        """
        raise NotImplementedError()

    @abstractmethod
    def get_day(self) -> int:
        """
        Возвращает текущий день (от установленного пользователем)
        """
        raise NotImplementedError()

    @abstractmethod
    def get_day_night_division(self) -> DayNightDivision:
        """
        Возвращает текущее время суток (день / ночь)
        """
        raise NotImplementedError()
