from vyzor.experiments import CPUStressExperiment
from vyzor.experiments.memory_stress import MemoryStressExperiment

EXPERIMENT_REGISTRY = {
    "cpu-stress": CPUStressExperiment,
    "memory-stress": MemoryStressExperiment,
}