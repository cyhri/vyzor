import os
import tempfile
import time

from vyzor.experiments.base import BaseExperiment


class DiskStressExperiment(BaseExperiment):

    name = "disk-stress"

    description = (
        "Generate temporary disk I/O "
        "for a configurable duration."
    )

    category = "resource"

    risk_level = "medium"

    def execute(self, **kwargs):

        size = kwargs.get("size", 100)

        duration = kwargs.get("duration", 10)

        print(f"Writing {size} MB to disk...")

        with tempfile.NamedTemporaryFile(delete=False) as file:

            file.write(b"\0" * size * 1024 * 1024)

            filename = file.name

        time.sleep(duration)

        os.remove(filename)

        print("Temporary file removed.")