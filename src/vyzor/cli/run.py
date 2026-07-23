import typer

from vyzor.engine.exceptions import ExperimentNotFoundError
from vyzor.engine.resolver import resolve_experiment


def run(
    experiment: str = typer.Argument(..., help="Experiment name"),
    duration: int = typer.Option(
        10,
        "--duration",
        "-d",
        min=1,
        help="Duration in seconds",
    ),
    workers: int | None = typer.Option(
        None,
        "--workers",
        "-w",
        help="Number of worker processes",
    ),
    memory: int = typer.Option(
        256,
        "--memory",
        "-m",
        min=1,
        help="Memory to allocate in MB.",
    ),
):
    try:
        experiment_cls = resolve_experiment(experiment)

        experiment = experiment_cls()

        if experiment.name == "memory-stress":
           experiment.execute(
           memory=memory,
           duration=duration,
    )
        else:
           experiment.execute(
           duration=duration,
           workers=workers,
    )      

    except ExperimentNotFoundError as error:
        typer.echo(error)