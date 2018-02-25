from typing import Iterable, Tuple

import psutil

from myconky.core.receipt import AbstractRepecit
from myconky.core.utils import gauge, bytes_fmt


class RamRecepit(AbstractRepecit):
    def get_info(self) -> Iterable[Tuple[str, str]]:
        mem = psutil.virtual_memory()
        yield (
            "RAM",
            gauge((mem.used/mem.total) * 100, summary="%s/%s" % (bytes_fmt(mem.used), bytes_fmt(mem.total))),
        )

        mem = psutil.swap_memory()
        if mem.total:
            yield (
                "SWAP",
                gauge((mem.used/mem.total) * 100, summary="%s/%s" % (bytes_fmt(mem.used), bytes_fmt(mem.total))),
            )
