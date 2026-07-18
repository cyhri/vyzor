import typer

from vyzor.engine.exceptions import ExperimentNotFoundError
from vyzor.engine.resolver import resolve_experiment

app = typer.Typer(
    help="Validate resilience by simulating controlled failures across multiple platforms.",
    invoke_without_command=False,
    no_args_is_help=True,
)


@app.command()
def run(experiment_name: str):
    """
    Execute a registered chaos experiment.
    """
    try:
        experiment = resolve_experiment(experiment_name)
        typer.echo(f"Resolved experiment: {experiment}")

    except ExperimentNotFoundError as error:
        typer.echo(error)


if __name__ == "__main__":
    app()