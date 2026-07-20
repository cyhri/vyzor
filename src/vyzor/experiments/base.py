from abc import ABC, abstractmethod


class BaseExperiment(ABC):
    """Base class for all chaos experiments."""
    
    name: str
    description: str
    category: str
    risk_level: str

    @abstractmethod
    def execute(self):
        """Execute the experiment."""
        pass