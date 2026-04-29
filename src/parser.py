import re

LOG_PATTERN = re.compile(
	r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>.*?)\] '
    	r'"(?P<method>\S+) (?P<path>\S+) (?P<protocol>.*?)" '
    	r'(?P<status>\d{3}) (?P<bytes>\d+)'
)

def parse_log_line(line: str):
	match = LOG_PATTERN.match(line.strip())
	if not match:
		return None

	data = match.groupdict()
	data["status"] = int(data["status"])
	data["bytes"] = int(data["bytes"])
	return data

def parse_log_file(file_path: str):
	parsed_logs = []
	failed_lines = []

	with open(file_path, "r", encoding="utf-8") as file:
		for line_number, line in enumerate(file, start=1):
			parsed = parse_log_line(line)
			if parsed:
				parsed_logs.append(parsed)
			else:
				failed_lines.append({"line_number": line_number, "raw": line.strip()})

	return parsed_logs, failed_lines
