import typer
from vyzor.engine.resolver import list_experiments

app = typer.Typer(
    help="Browse available chaos experiments."
)


@app.callback(invoke_without_command=True)
def catalog():
    typer.echo("\nAvailable Experiments\n")

    for experiment in list_experiments():
        typer.echo(f"{experiment.name}")
        typer.echo(f"{experiment.description}")
        typer.echo(f"  Category : {experiment.category}")
        typer.echo(f"  Risk     : {experiment.risk_level}")
        typer.echo()