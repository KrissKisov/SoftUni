from project.software.software import Software


class ExpressSoftware(Software):

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Express", int(capacity_consumption), int(memory_consumption * 2))
