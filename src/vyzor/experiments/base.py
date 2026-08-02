from abc import ABC, abstractmethod


class BaseExperiment(ABC):

    name = ""

    description = ""

    category = ""

    risk_level = ""

    def before_execute(self):
        """Hook executed before the experiment."""
        pass

    @abstractmethod
    def execute(self, **kwargs):
        """Execute the experiment."""
        pass

    def after_execute(self):
        """Hook executed after the experiment."""
        pass