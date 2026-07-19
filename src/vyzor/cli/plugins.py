import typer

app = typer.Typer(
    help="Manage plugins."
)


@app.callback(invoke_without_command=True)
def plugins():
    typer.echo("Plugins command coming soon...")