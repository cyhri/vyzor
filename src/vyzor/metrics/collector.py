import multiprocessing
import platform
import sys
import time


class MetricsCollector:
    """Collect execution metrics."""

    def __init__(self):
        self._start_time = None

    def start(self):
        """Start metrics collection."""
        self._start_time = time.perf_counter()

    def stop(self):
        """Stop metrics collection and return metrics."""

        execution_time = round(
            time.perf_counter() - self._start_time,
            2,
        )

        return {
            "execution_time": execution_time,
            "platform": platform.system(),
            "python_version": platform.python_version(),
            "cpu_count": multiprocessing.cpu_count(),
        }