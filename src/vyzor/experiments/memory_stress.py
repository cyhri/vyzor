import time

from vyzor.experiments.base import BaseExperiment


class MemoryStressExperiment(BaseExperiment):
    name = "memory-stress"

    description = (
        "Consume a configurable amount "
        "of system memory for a specified duration."
    )

    category = "resource"

    risk_level = "medium"

    def execute(
        self,
        memory: int = 256,
        duration: int = 10,
    ):
        print(f"Allocating {memory} MB of memory...")

        allocated = bytearray(memory * 1024 * 1024)

        time.sleep(duration)

        del allocated

        print("Memory released.")