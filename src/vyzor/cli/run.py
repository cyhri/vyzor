import typer

from vyzor.engine.resolver import resolve_experiment
from vyzor.engine.exceptions import ExperimentNotFoundError

app = typer.Typer(help="Run chaos experiments.")


@app.callback(invoke_without_command=True)
def run(
    experiment: str = typer.Argument(...),
):
    try:
        experiment_cls = resolve_experiment(experiment)

        experiment_instance = experiment_cls()

        experiment_instance.execute()

    except ExperimentNotFoundError as error:
        typer.echo(error)