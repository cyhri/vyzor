import typer

app = typer.Typer(
    help="Browse available chaos experiments."
)


@app.callback(invoke_without_command=True)
def catalog():
    typer.echo("Catalog command coming soon...")