import argparse

def build_cli():
	parser = argparse.ArgumentParser(
		description = "Parse Apache logs and detect suspicious activity"
	)

	parser.add_argument(
		"--input",
		required=True,
		help="Path to input log file"
	)

	parser.add_argument(
		"--rules",
		required=True,
		help="Path to detection rules JSON file"
	)

	return parser
