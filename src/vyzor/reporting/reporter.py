import json
from pathlib import Path
from datetime import datetime


class ExperimentReporter:

    def save_report(
        self,
        experiment: str,
        success: bool,
        duration: int,
    ):

        report = {
            "experiment": experiment,
            "success": success,
            "duration": duration,
            "timestamp": datetime.now().isoformat(),
        }

        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)

        filename = (
            reports_dir
            / f"{experiment}-{int(datetime.now().timestamp())}.json"
        )

        with open(filename, "w") as file:
            json.dump(
                report,
                file,
                indent=4,
            )

        print(f"Report saved: {filename}")