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
    """CPU stress experiment."""

    name = "cpu-stress"

    description = (
        "Generate sustained CPU load "
        "for a configurable duration."
    )

    category = "resource"

    risk_level = "medium"

    def before_execute(self):
        """Hook executed before the experiment."""
        pass

    def execute(self, **kwargs):
        """Execute the CPU stress experiment."""

        duration = kwargs.get("duration", 10)
        workers = kwargs.get("workers")

        cpu_count = workers or multiprocessing.cpu_count()

        print(f"Duration : {duration}s")
        print(f"Workers  : {cpu_count}")

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

        print("CPU stress execution completed.")

    def after_execute(self):
        """Hook executed after the experiment."""
        pass