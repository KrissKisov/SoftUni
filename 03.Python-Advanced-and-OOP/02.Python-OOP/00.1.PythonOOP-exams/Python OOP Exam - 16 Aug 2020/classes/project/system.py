from typing import List
from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        phw = PowerHardware(name, capacity, memory)
        System._hardware.append(phw)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hhw = HeavyHardware(name, capacity, memory)
        System._hardware.append(hhw)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = next(filter(lambda x: x.name == hardware_name, System._hardware))
            exp_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(exp_software)
            System._software.append(exp_software)

        except StopIteration:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = next(filter(lambda x: x.name == hardware_name, System._hardware))
            light_software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(light_software)
            System._software.append(light_software)

        except StopIteration:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return (f"System Analysis\n"
                f"Hardware Components: {len(System._hardware)}\n"
                f"Software Components: {len(System._software)}\n"
                f"Total Operational Memory: {sum([s.memory_consumption for s in System._software])} "
                f"/ {sum([h.memory for h in System._hardware])}\n"
                f"Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])} "
                f"/ {sum([h.capacity for h in System._hardware])}")

    @staticmethod
    def system_split():
        result = ""

        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            result += f"Express Software Components: {len([s for s in hardware.software_components if s.software_type == 'Express'])}\n"
            result += f"Light Software Components: {len([s for s in hardware.software_components if s.software_type == 'Light'])}\n"
            result += f"Memory Usage: {sum([s.memory_consumption for s in hardware.software_components])} / {hardware.memory}\n"
            result += f"Capacity Usage: {sum([s.capacity_consumption for s in hardware.software_components])} / {hardware.capacity}\n"
            result += f"Type: {hardware.hardware_type}\n"
            result += f"Software Components: {', '.join([sc.name for sc in hardware.software_components]) if len(hardware.software_components) > 0 else 'None'}\n"

        return result[:-1]
