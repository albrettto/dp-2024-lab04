import unittest
from unittest.mock import MagicMock
from datetime import datetime
from clocks.clock_adapter import ClockAdapter
from clocks.analog_clock import AnalogClock
from consts import DayNightDivision


class TestClockAdapter(unittest.TestCase):

    def setUp(self):
        # Создаем макет аналоговых часов
        self.analog_clock_mock = MagicMock(spec=AnalogClock)
        # Создаем адаптер с макетом
        self.clock_adapter = ClockAdapter(self.analog_clock_mock)

    def test_set_date_time_am(self):
        """Проверяет корректную установку времени для утреннего времени (AM)."""
        date = datetime(2024, 11, 5, 9, 30, 15)  # 09:30:15 AM
        self.clock_adapter.set_date_time(date)

        expected_hour_angle = 9 * 30 + 30 / 60 * 30  # Угол часовой стрелки с учетом минут
        expected_minute_angle = 30 * 6 + 15 / 60 * 6  # Угол минутной стрелки с учетом секунд
        expected_second_angle = 15 * 6

        self.analog_clock_mock.set_date_time.assert_called_once_with(
            2024, 11, 5, expected_hour_angle, expected_minute_angle, expected_second_angle, DayNightDivision.AM
        )

    def test_set_date_time_pm(self):
        """Проверяет корректную установку времени для дневного времени (PM)."""
        date = datetime(2024, 11, 5, 15, 45, 10)  # 03:45:10 PM
        self.clock_adapter.set_date_time(date)

        expected_hour_angle = 3 * 30 + 45 / 60 * 30
        expected_minute_angle = 45 * 6 + 10 / 60 * 6
        expected_second_angle = 10 * 6

        self.analog_clock_mock.set_date_time.assert_called_once_with(
            2024, 11, 5, expected_hour_angle, expected_minute_angle, expected_second_angle, DayNightDivision.PM
        )

    def test_set_date_time_midnight(self):
        """Проверяет корректную установку времени для полуночи (00:00:00 AM)."""
        date = datetime(2024, 11, 5, 0, 0, 0)  # 00:00:00 AM
        self.clock_adapter.set_date_time(date)

        self.analog_clock_mock.set_date_time.assert_called_once_with(
            2024, 11, 5, 0, 0, 0, DayNightDivision.AM
        )

    def test_set_date_time_noon(self):
        """Проверяет корректную установку времени для полудня (12:00:00 PM)."""
        date = datetime(2024, 11, 5, 12, 0, 0)  # 12:00 PM
        self.clock_adapter.set_date_time(date)

        expected_hour_angle = 0  # На аналоговых часах полдень эквивалентен 0 градусов для часа

        self.analog_clock_mock.set_date_time.assert_called_once_with(
            2024, 11, 5, expected_hour_angle, 0, 0, DayNightDivision.PM
        )

    def test_get_date_time_am(self):
        """Проверяет корректное получение времени в формате datetime для утреннего времени (AM)."""
        # Настраиваем возвращаемые значения от mock-объекта для утреннего времени
        self.analog_clock_mock.get_year.return_value = 2024
        self.analog_clock_mock.get_month.return_value = 11
        self.analog_clock_mock.get_day.return_value = 5
        self.analog_clock_mock.get_hour_angle.return_value = 270  # 9:00 AM
        self.analog_clock_mock.get_minute_angle.return_value = 180  # 30 минут
        self.analog_clock_mock.get_second_angle.return_value = 90  # 15 секунд
        self.analog_clock_mock.get_day_night_division.return_value = DayNightDivision.AM

        result = self.clock_adapter.get_date_time()
        self.assertEqual(result, datetime(2024, 11, 5, 9, 30, 15))

    def test_get_date_time_pm(self):
        """Проверяет корректное получение времени в формате datetime для дневного времени (PM)."""
        self.analog_clock_mock.get_year.return_value = 2024
        self.analog_clock_mock.get_month.return_value = 11
        self.analog_clock_mock.get_day.return_value = 5
        self.analog_clock_mock.get_hour_angle.return_value = 90  # 3:00 PM
        self.analog_clock_mock.get_minute_angle.return_value = 270  # 45 минут
        self.analog_clock_mock.get_second_angle.return_value = 60  # 10 секунд
        self.analog_clock_mock.get_day_night_division.return_value = DayNightDivision.PM

        result = self.clock_adapter.get_date_time()
        self.assertEqual(result, datetime(2024, 11, 5, 15, 45, 10))

    def test_get_date_time_midnight(self):
        """Проверяет корректное получение времени в формате datetime для полуночи (AM)."""
        self.analog_clock_mock.get_year.return_value = 2024
        self.analog_clock_mock.get_month.return_value = 11
        self.analog_clock_mock.get_day.return_value = 5
        self.analog_clock_mock.get_hour_angle.return_value = 0  # 0 часов
        self.analog_clock_mock.get_minute_angle.return_value = 0  # 0 минут
        self.analog_clock_mock.get_second_angle.return_value = 0  # 0 секунд
        self.analog_clock_mock.get_day_night_division.return_value = DayNightDivision.AM

        result = self.clock_adapter.get_date_time()
        self.assertEqual(result, datetime(2024, 11, 5, 0, 0, 0))

    def test_get_date_time_noon(self):
        """Проверяет корректное получение времени в формате datetime для полудня (PM)."""
        self.analog_clock_mock.get_year.return_value = 2024
        self.analog_clock_mock.get_month.return_value = 11
        self.analog_clock_mock.get_day.return_value = 5
        self.analog_clock_mock.get_hour_angle.return_value = 0
        self.analog_clock_mock.get_minute_angle.return_value = 0
        self.analog_clock_mock.get_second_angle.return_value = 0
        self.analog_clock_mock.get_day_night_division.return_value = DayNightDivision.PM

        result = self.clock_adapter.get_date_time()
        self.assertEqual(result, datetime(2024, 11, 5, 12, 0, 0))


if __name__ == "__main__":
    unittest.main()
