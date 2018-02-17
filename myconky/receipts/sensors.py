from typing import Iterable, Tuple

import psutil

from myconky.core.receipt import AbstractRepecit
from myconky.core.utils import gauge, bytes_fmt


class SensorsRecepit(AbstractRepecit):
    def get_info(self) -> Iterable[Tuple[str, str]]:
        for name, sensors in psutil.sensors_temperatures().items():
            for s in sensors:
                yield (
                    "%s %s" % (name, s.label),
                    "%s C" % str(s.current),
                )
