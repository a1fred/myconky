from typing import Iterable, Tuple

import psutil

from sysinfo_recepits.core.receipt import AbstractRepecit
from sysinfo_recepits.core.utils import gauge, bytes_fmt


class BatteryRecepit(AbstractRepecit):
    def get_info(self) -> Iterable[Tuple[str, str]]:
        battery = psutil.sensors_battery()
        label = "Battery"
        if battery.power_plugged:
            label += " (c)"
        yield (
            label,
            gauge(battery.percent)
        )

        if not battery.power_plugged:
            time_left = battery.secsleft
            if time_left not in [psutil.POWER_TIME_UNKNOWN, psutil.POWER_TIME_UNLIMITED]:
                yield (
                    "",
                    "%sm left" % str(int(time_left/60))
                )
