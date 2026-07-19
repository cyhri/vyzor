import typer

app = typer.Typer(
    help="Manage execution targets."
)


@app.callback(invoke_without_command=True)
def targets():
    typer.echo("Targets command coming soon...")