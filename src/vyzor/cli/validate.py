import typer

app = typer.Typer(
    help="Validate experiment configurations."
)


@app.callback(invoke_without_command=True)
def validate():
    typer.echo("Validate command coming soon...")