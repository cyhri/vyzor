import time

from vyzor.experiments.base import BaseExperiment


class NetworkLatencyExperiment(BaseExperiment):

    name = "network-latency"

    description = (
        "Simulate network latency "
        "for a configurable duration."
    )

    category = "network"

    risk_level = "low"

    def execute(self, **kwargs):

        latency = kwargs.get("latency", 100)

        duration = kwargs.get("duration", 10)

        print(
            f"Simulating {latency} ms latency "
            f"for {duration} seconds..."
        )

        time.sleep(duration)

        print("Network latency simulation completed.")