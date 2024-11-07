import datetime
from clocks.analog_clock import AnalogClock
from clocks.clock_adapter import ClockAdapter

if __name__ == "__main__":
    clock_adapter = ClockAdapter(AnalogClock())
    print(clock_adapter.get_date_time())

    print()

    clock_adapter.set_date_time(datetime.datetime.now())
    print(clock_adapter.get_date_time())
