from src.parser import parse_log_file

def test_parse_log_line_success():
	line = '192.168.1.10 - - [25/Apr/2026:09:00:01 +0530] "GET /index.html HTTP/1.1" 200 1024'
	parsed = parse_log_line(line)

	assert parsed is not None
	assert parsed["ip"] == "192.168.1.10"
	assert parsed["method"] == "GET"
	assert parsed["path"] == "/index.html"
	assert parsed["status"] == 200


