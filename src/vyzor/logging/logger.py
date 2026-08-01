from datetime import datetime
from pathlib import Path


class ExperimentLogger:

    def log(
        self,
        experiment: str,
        status: str,
    ):

        logs_dir = Path("logs")
        logs_dir.mkdir(exist_ok=True)

        logfile = (
            logs_dir
            / f"{datetime.now().strftime('%Y-%m-%d')}.log"
        )

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(logfile, "a") as file:
            file.write(
                f"[{timestamp}] "
                f"{experiment.upper()} "
                f"{status.upper()}\n"
            )

        print(f"Log updated: {logfile}")