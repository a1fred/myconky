import monotable.table
from sysinfo_recepits.receipts import (
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
    print(monotable.table.table(cellgrid=get_cells()))

