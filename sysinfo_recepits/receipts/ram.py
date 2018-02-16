from typing import Iterable, Tuple

import psutil

from sysinfo_recepits.core.receipt import AbstractRepecit
from sysinfo_recepits.core.utils import gauge, bytes_fmt


class RamRecepit(AbstractRepecit):
    def get_info(self) -> Iterable[Tuple[str, str]]:
        mem = psutil.virtual_memory()
        yield (
            "RAM",
            gauge((mem.used/mem.total) * 100, summary="%s/%s" % (bytes_fmt(mem.used), bytes_fmt(mem.total))),
        )

        mem = psutil.swap_memory()
        yield (
            "SWAP",
            gauge((mem.used/mem.total) * 100, summary="%s/%s" % (bytes_fmt(mem.used), bytes_fmt(mem.total))),
        )
