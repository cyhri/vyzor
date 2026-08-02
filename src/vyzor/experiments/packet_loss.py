import random
import time

from vyzor.experiments.base import BaseExperiment


class PacketLossExperiment(BaseExperiment):
    """Packet loss simulation experiment."""

    name = "packet-loss"

    description = (
        "Simulate packet loss "
        "for a configurable duration."
    )

    category = "network"

    risk_level = "low"

    def before_execute(self):
        """Hook executed before the experiment."""
        pass

    def execute(self, **kwargs):
        """Execute the packet loss simulation."""

        duration = kwargs.get("duration", 10)

        loss = kwargs.get("loss", 10)

        print(f"Duration : {duration}s")
        print(f"Loss     : {loss}%")

        end_time = time.time() + duration

        sent = 0
        dropped = 0

        while time.time() < end_time:

            sent += 1

            if random.randint(1, 100) <= loss:
                dropped += 1

            time.sleep(0.05)

        delivered = sent - dropped

        print(f"Packets Sent      : {sent}")
        print(f"Packets Delivered : {delivered}")
        print(f"Packets Dropped   : {dropped}")

    def after_execute(self):
        """Hook executed after the experiment."""
        pass