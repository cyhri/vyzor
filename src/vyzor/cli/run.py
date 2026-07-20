import typer

from vyzor.engine.exceptions import ExperimentNotFoundError
from vyzor.engine.resolver import resolve_experiment

app = typer.Typer(help="Run chaos experiments.")


@app.callback()
def execute(
    experiment: str = typer.Argument(..., help="Experiment name"),
    duration: int = typer.Option(
        10,
        "--duration",
        "-d",
        min=1,
        help="Duration in seconds",
    ),
    workers: int = typer.Option(
        None,
        "--workers",
        "-w",
        help="Number of worker processes",
    ),
):
    try:
        experiment_cls = resolve_experiment(experiment)

        experiment = experiment_cls()

        experiment.execute(
            duration=duration,
            workers=workers,
        )

    except ExperimentNotFoundError as error:
        typer.echo(error)