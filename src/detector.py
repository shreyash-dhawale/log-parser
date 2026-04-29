from collections import Counter

def detect_failed_logins(records: list, threshold: int) -> list:
	failed_login_ips = [
		record["ip"]
		for record in records
		if record["path"] == "/login" and record["status"] == 401
	]
	counts = Counter(failed_login_ips)

	alerts = []
	for ip, count in counts.items():
		if count >= threshold:
			alerts.append({
				"type" : "failed_login_bruteforce",
				"ip" : ip,
				"count" : count,
				"message" : f"{ip} has {count} failed login attempts"
})

	return alerts

def detect_suspicious_paths(records: list, suspicious_paths: list) -> list:
	alerts = []

	for record in records:
		if record["path"] in suspicious_paths:
			alerts.append({
				"type" : "suspicious_path_access",
				"ip" : record["ip"],
				"path" : record["path"],
				"status" : record["status"],
				"message" : f"Suspicious path accessed: {record['path']} from {record['ip']}"
			})
	return alerts

def run_detections(records: list, rules: dict) -> list:
	alerts = []
	alerts.extend(
		detect_failed_logins(records, rules["failed_login_threshold"])
	)
	alerts.extend(
		detect_suspicious_paths(records, rules["suspicious_paths"])
	)
	return alerts

