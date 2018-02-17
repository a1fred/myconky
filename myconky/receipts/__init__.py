from myconky.receipts import (
    cpu,
    ram,
    disk_space,
    network_interfaces,
    sensors,
    battery,
)


RECEIPTS_MAPPING = {
    'cpu': cpu.CpuRecepit,
    'ram': ram.RamRecepit,
    'disk_space': disk_space.DiskSpaceRecepit,
    'network_interfaces': network_interfaces.NetworkInterfacesRecepit,
    'sensors': sensors.SensorsRecepit,
    'battery': battery.BatteryRecepit,
}
