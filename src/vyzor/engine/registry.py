from vyzor.experiments.cpu_stress import CPUStressExperiment
from vyzor.experiments.memory_stress import MemoryStressExperiment
from vyzor.experiments.disk_stress import DiskStressExperiment
from vyzor.experiments.network_latency import NetworkLatencyExperiment
from vyzor.experiments.packet_loss import PacketLossExperiment

EXPERIMENT_REGISTRY = {
    "cpu-stress": CPUStressExperiment,
    "memory-stress": MemoryStressExperiment,
    "disk-stress": DiskStressExperiment,
    "network-latency": NetworkLatencyExperiment,
    "packet-loss": PacketLossExperiment,
}