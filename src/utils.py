import json
import os

def ensure_directory(path: str) -> None:
	os.makedirs(path, exist_ok=True)


def load_json_file(path: str):
	with open(path, "r", encoding="utf-8") as file:
		return json.load(file)


def save_json_file(path: str, data) -> None:
	with open(path, "w", encoding="utf-8") as file:
		json.dump(data, file, indent=4)
