import typer

app = typer.Typer(
    help="Validate resilience by simulating controlled failures across multiple platforms."
)

@app.command()
def run(experiment_name: str):
    """
    Execute a registered chaos experiment.
    """
    print(f"Running experiment: {experiment_name}")


if __name__ == "__main__":
    app()