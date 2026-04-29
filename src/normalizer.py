from datetime import datetime

def normalize_record(record: dict) -> dict:
	normalized = record.copy()

	raw_timestamp = normalized["timestamp"]
	dt = datetime.strptime(raw_timestamp, "%d/%b/%Y:%H:%M:%S %z")
	normalized["timestamp"] = dt.isoformat()

	normalized["method"] = normalized["method"].upper()
	normalized["path"] = normalized["path"].lower()
	normalized["protocol"] = normalized["protocol"].upper()

	return normalized

def normalize_records(records: list) -> list:
	return [normalize_record(record) for record in records]
