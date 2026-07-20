from vyzor.engine.exceptions import ExperimentNotFoundError
from vyzor.engine.registry import EXPERIMENT_REGISTRY


def resolve_experiment(experiment_name: str):
    try:
        return EXPERIMENT_REGISTRY[experiment_name]
    except KeyError:
        raise ExperimentNotFoundError(experiment_name)
    
def list_experiments():
    return [
        experiment()
        for experiment in EXPERIMENT_REGISTRY.values()
    ]