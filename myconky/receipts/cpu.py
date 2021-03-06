from typing import Iterable, Tuple

import psutil

from myconky.core.receipt import AbstractRepecit
from myconky.core.utils import gauge


class CpuRecepit(AbstractRepecit):
    def get_info(self) -> Iterable[Tuple[str, str]]:
        corenum = 0
        for cpuload in psutil.cpu_percent(interval=1, percpu=True):
            corenum += 1
            yield ("CPU%s" % str(corenum), gauge(cpuload))
