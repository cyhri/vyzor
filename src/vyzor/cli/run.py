import typer

from vyzor.engine.exceptions import ExperimentNotFoundError
from vyzor.engine.resolver import resolve_experiment

app = typer.Typer(
    invoke_without_command=True,
    no_args_is_help=True,
)


@app.callback()
def run(experiment_name: str):
    """
    Execute a registered chaos experiment.
    """
    try:
        experiment = resolve_experiment(experiment_name)
        typer.echo(f"Resolved experiment: {experiment}")

    except ExperimentNotFoundError as error:
        typer.echo(error)