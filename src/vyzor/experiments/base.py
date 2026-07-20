from abc import ABC, abstractmethod


class BaseExperiment(ABC):
    """Base class for all chaos experiments."""

    name: str

    @abstractmethod
    def execute(self):
        """Execute the experiment."""
        pass