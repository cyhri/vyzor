class ExperimentNotFoundError(Exception):
    """Raised when an experiment is not found in the registry."""

    def __init__(self, experiment_name: str):
        self.experiment_name = experiment_name
        super().__init__(f"Unknown experiment: {experiment_name}")