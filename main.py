import logging
from config.settings import OUTPUT_DIR
from src.cli import build_cli
from src.normalizer import normalize_records
from src.parser import parse_log_file
from src.detector import run_detections
from src.reporter import write_csv, write_markdown_report
from src.utils import ensure_directory, load_json_file, save_json_file

logging.basicConfig(
	level = logging.INFO,
	format = "%(asctime)s - %(levelname)s - %(message)s"
)

def main():
	parser = build_cli()
	args = parser.parse_args()

	ensure_directory(OUTPUT_DIR)

	logging.info("Loading rules")
	rules = load_json_file(args.rules)

	logging.info("Parsing log file")
	parsed_logs, failed_logs = parse_log_file(args.input)

	logging.info("Normalizing records")
	normalized_logs = normalize_records(parsed_logs)

	logging.info("Running detections")
	alerts = run_detections(normalized_logs, rules)

	logging.info("Writing outputs")
	write_csv(normalized_logs, f"{OUTPUT_DIR}/parsed_logs.csv")
	save_json_file(f"{OUTPUT_DIR}/alerts.json", alerts)
	write_markdown_report(
		normalized_logs,
		alerts,
		failed_logs,
		f"{OUTPUT_DIR}/summary_report.md"
	)

	logging.info("Done. Reports saved in output/")


if __name__ == "__main__":
	main()
