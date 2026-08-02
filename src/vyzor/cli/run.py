import typer

from vyzor.engine.exceptions import ExperimentNotFoundError
from vyzor.engine.resolver import resolve_experiment
from vyzor.logging.logger import ExperimentLogger
from vyzor.reporting.reporter import ExperimentReporter


def run(
    experiment: str = typer.Argument(..., help="Experiment name"),
    duration: int = typer.Option(
        10,
        "--duration",
        "-d",
        min=1,
        help="Duration in seconds",
    ),
    workers: int | None = typer.Option(
         None,
         "--workers",
         "-w",
         help="Number of worker processes",
    ),
    memory: int = typer.Option(
         256,
         "--memory",
         "-m",
         min=1,
         help="Memory to allocate in MB.",
    ),
    size: int = typer.Option(
         100,
         "--size",
         "-s",
         min=1,
         help="Disk usage in MB.",
    ),
    latency: int = typer.Option(
        100,
        "--latency",
        "-l",
        min=1,
        help="Latency in milliseconds.",
    ),
):
    try:
        experiment_cls = resolve_experiment(experiment)

        experiment = experiment_cls()

        experiment.before_execute()

        experiment.execute(
            duration=duration,
            workers=workers,
            memory=memory,
            size=size,
            latency=latency,
    )

        experiment.after_execute()
        
        reporter = ExperimentReporter()

        reporter.save_report(
            experiment=experiment.name,
            success=True,
            duration=duration,
)

        logger = ExperimentLogger()

        logger.log(
        experiment=experiment.name,
        status="completed",
)

    except ExperimentNotFoundError as error:
        typer.echo(error)