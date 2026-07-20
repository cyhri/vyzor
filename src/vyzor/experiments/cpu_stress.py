import math
import multiprocessing
import time

from vyzor.experiments.base import BaseExperiment


def _stress_worker(duration: int):
    """Consume CPU for the specified duration."""
    end_time = time.time() + duration

    while time.time() < end_time:
        math.sqrt(987654321)


class CPUStressExperiment(BaseExperiment):
    name = "cpu-stress"

    description = (
        "Generate sustained CPU load "
        "for a configurable duration."
    )

    category = "resource"

    risk_level = "medium"

    def execute(self, duration: int = 10, workers: int | None = None,):
        cpu_count = workers or multiprocessing.cpu_count()

        print(f"Starting CPU stress on {cpu_count} cores...")
        print(f"Duration: {duration}s")
        print(f"Workers : {cpu_count}")

        processes = []

        for _ in range(cpu_count):
            process = multiprocessing.Process(
                target=_stress_worker,
                args=(duration,),
            )
            process.start()
            processes.append(process)

        for process in processes:
            process.join()

        print("CPU stress experiment completed.")