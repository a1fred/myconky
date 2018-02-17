from typing import Iterable, Tuple

from platform import system
import psutil

from myconky.core.receipt import AbstractRepecit
from myconky.core.utils import gauge, bytes_fmt


class DiskSpaceRecepit(AbstractRepecit):
    def get_info(self) -> Iterable[Tuple[str, str]]:
        for disk in psutil.disk_partitions(all=False):
            if system() == 'Darwin':
                if disk.mountpoint == '/private/var/vm':
                    continue

            usage = psutil.disk_usage(disk.mountpoint)

            if usage.total != 0:
                usage_perc = (usage.used/usage.total) * 100

                yield (
                    disk.mountpoint,
                    gauge(usage_perc, summary="%s/%s" % (bytes_fmt(usage.used), bytes_fmt(usage.total))),
                )
