import typer

app = typer.Typer(
    help="Manage experiment reports."
)


@app.callback(invoke_without_command=True)
def report():
    typer.echo("Report command coming soon...")