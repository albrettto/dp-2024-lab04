from consts.time_consts import TimeConsts
from consts import DayNightDivision


class TimeConverter:
    """
    Класс для преобразования времени между углами стрелок аналоговых часов и стандартными единицами времени (часы, минуты, секунды).
    """

    @staticmethod
    def hour_to_angle(hour: int, minute: int) -> float:
        """
        Преобразует время в часах и минутах в угол для часовой стрелки на аналоговых часах.
        Метод также учитывает сдвиг часовой стрелки за счет минут.

        Args:
            hour (int): Часы (от 0 до 23).
            minute (int): Минуты (от 0 до 59).

        Returns:
            float: Угол в градусах для часовой стрелки.
        """
        # Получаем угол стрелки часа не учитывая смещение по минутам
        hour_angle = hour % TimeConsts.HOURS * TimeConsts.DEG_FOR_HOUR

        # Получаем смещение стрелки по минутам
        minute_offset = minute / TimeConsts.MIN * TimeConsts.DEG_FOR_HOUR

        return hour_angle + minute_offset

    @staticmethod
    def minute_to_angle(minute: int, second: int) -> float:
        """
        Преобразует время в минутах и секундах в угол для минутной стрелки на аналоговых часах.
        Метод также учитывает сдвиг минутной стрелки за счет секунд.

        Args:
            minute (int): Минуты (от 0 до 59).
            second (int): Секунды (от 0 до 59).

        Returns:
            float: Угол в градусах для минутной стрелки.
        """
        # Получаем угол минутной стрелки не учитывая смещение по секундам
        minute_angle = minute * TimeConsts.DEG_FOR_MIN

        # Получаем смещение стрелки по секундам
        second_offset = second / TimeConsts.SEC * TimeConsts.DEG_FOR_MIN

        return minute_angle + second_offset

    @staticmethod
    def angle_to_hour(hour_angle: float, day_night_division: DayNightDivision) -> int:
        """
        Преобразует угол часовой стрелки обратно в часы.

        Args:
            hour_angle (float): Угол в градусах для часовой стрелки.
            day_night_division (DayNightDivision): Текущее время суток: AM - день; PM - вечер.

        Returns:
            int: Число часов (от 0 до 23).
        """
        hour = int(hour_angle / TimeConsts.DEG_FOR_HOUR)
        if day_night_division == DayNightDivision.PM and hour != 12:
            hour += 12
        elif day_night_division == DayNightDivision.AM and hour == 12:
            hour = 0
        return hour

    @staticmethod
    def angle_to_minute(minute_angle: float) -> int:
        """
        Преобразует угол минутной стрелки обратно в минуты.

        Args:
            minute_angle (float): Угол в градусах для минутной стрелки.

        Returns:
            int: Число минут (от 0 до 59).
        """
        return int(minute_angle / TimeConsts.DEG_FOR_SEC)
