import time

from vyzor.experiments.base import BaseExperiment


class MemoryGrowthExperiment(BaseExperiment):
    """Memory growth simulation experiment."""

    name = "memory-growth"

    description = (
        "Simulate controlled memory growth "
        "for a configurable duration."
    )

    category = "resource"

    risk_level = "medium"

    def before_execute(self):
        """Hook executed before the experiment."""
        pass

    def execute(self, **kwargs):
        """Execute the memory growth simulation."""

        duration = kwargs.get("duration", 10)
        step = kwargs.get("step", 32)

        print(f"Duration : {duration}s")
        print(f"Step Size: {step} MB")

        allocated = []
        end_time = time.time() + duration

        while time.time() < end_time:

            allocated.append(bytearray(step * 1024 * 1024))

            print(
                f"Allocated : {len(allocated) * step} MB"
            )

            time.sleep(1)

        allocated.clear()

        print("Memory growth simulation completed.")

    def after_execute(self):
        """Hook executed after the experiment."""
        pass