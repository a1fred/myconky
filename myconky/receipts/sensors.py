from typing import Iterable, Tuple

import psutil
import oscheck

from myconky.core.receipt import AbstractRepecit


class SensorsRecepit(AbstractRepecit):
    @classmethod
    def is_supported(cls) -> bool:
        if oscheck.family() not in [oscheck.OS_LINUX, ]:
            return False
        return True

    def get_info(self) -> Iterable[Tuple[str, str]]:
        for name, sensors in psutil.sensors_temperatures().items():
            for s in sensors:
                yield (
                    "%s %s" % (name, s.label),
                    "%s C" % str(s.current),
                )
