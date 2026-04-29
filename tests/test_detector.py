from src.detector import detect_failed_logins

def test_detect_failed_logins():
	records = [
		{"ip": "192.168.1.15", "path": "/login", "status": 401},
        	{"ip": "192.168.1.15", "path": "/login", "status": 401},
        	{"ip": "192.168.1.15", "path": "/login", "status": 401}
	]

	alerts = detect_failed_logins(records, 3)

	assert len(alerts) == 1
	assert alerts[0]["type"] == "failed_login_bruteforce"
