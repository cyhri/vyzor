import typer

from vyzor.cli.run import run
from vyzor.cli.catalog import app as catalog_app
from vyzor.cli.plugins import app as plugins_app
from vyzor.cli.report import app as report_app
from vyzor.cli.targets import app as targets_app
from vyzor.cli.validate import app as validate_app

app = typer.Typer(
    help="Validate resilience by simulating controlled failures across multiple platforms.",
)

app.command(name="run")(run)

app.add_typer(catalog_app, name="catalog")
app.add_typer(plugins_app, name="plugins")
app.add_typer(report_app, name="report")
app.add_typer(targets_app, name="targets")
app.add_typer(validate_app, name="validate")

if __name__ == "__main__":
    app()