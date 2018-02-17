from myconky.core.utils import table
from myconky.receipts import (
    cpu,
    ram,
    disk_space,
    network_interfaces,
    sensors,
    battery,
)


RECEIPTS = [
    cpu.CpuRecepit(),
    ram.RamRecepit(),
    disk_space.DiskSpaceRecepit(),
    network_interfaces.NetworkInterfacesRecepit(),
    # sensors.SensorsRecepit(),
    battery.BatteryRecepit(),
]


def get_cells():
    for r in RECEIPTS:
        for n, g in r.get_info():
            yield (n, g)
        yield ("", "")


def main():
    print(table(cellgrid=get_cells()))
