import csv
from collections import Counter

def write_csv(records: list, output_file: str) -> None:
	if not records:
		return

	fieldnames = records[0].keys()

	with open(output_file, "w", newline="", encoding="utf-8") as file:
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(records)

def write_markdown_report(records: list, alerts: list, failed_lines: list, output_file: str) -> None:
	status_counter = Counter(record["status"] for record in records)
	ip_counter = Counter(record["ip"] for record in records)

	with open(output_file, "w", encoding="utf-8") as file:
		file.write("# Log Analysis Report\n\n")
		file.write(f"Total parsed records: {len(records)}\n\n")
		file.write(f"Total alerts: {len(alerts)}\n\n")
		file.write(f"Malformed lines: {len(failed_lines)}\n\n")

		file.write("## Top IPs\n")
		for ip, count in ip_counter.most_common(5):
			file.write(f"- {ip}: {count} requests")

		file.write("\n## Status Codes\n")
		for status, count in status_counter.items():
			file.write(f"- {status}: {count}\n")

		file.write("\n## Alerts\n")
		if alerts:
			for alert in alerts:
				file.write(f"- [{alert['type']}] {alert['message']}\n")
		else:
			file.write("- No suspicious activity detected\n")
