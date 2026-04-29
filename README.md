# Python Log Parser and Security Analyzer

## Overview
This project parses Apache access logs, converts them into structured records, detects suspicious activity, and generates reports.

## Features
- Regex-based Apache log parsing
- Timestamp normalization
- Failed login detection
- Suspicious path detection
- CSV, JSON, and Markdown output
- CLI support with argparse
- Unit tests with pytest

## How to Run
```bash
python main.py --input logs/sample_access.log --rules rules/detection_rules.json
```

## Output
- parsed_logs.csv
- alerts.json
- summary_report.md

## Future Improvements
- Add support for Nginx logs
- Add IP reputation lookups
- Add dashboard visualization
- Add Docker support
