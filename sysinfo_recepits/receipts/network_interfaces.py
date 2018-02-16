from typing import Iterable, Tuple

import psutil
import requests

from sysinfo_recepits.core.receipt import AbstractRepecit


class NetworkInterfacesRecepit(AbstractRepecit):
    def get_info(self) -> Iterable[Tuple[str, str]]:
        try:
            ext_ip = requests.get("http://www.myexternalip.com/raw").text
            yield (
                "External IP",
                ext_ip,
            )
        except:
            pass

        for iface, data in psutil.net_if_addrs().items():
            if iface != 'lo0':
                for addr in data:
                    if addr.address and addr.family == 2:
                        yield(iface, addr.address)
