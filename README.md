![Banner](banner.png)

# analyze-string-patterns
Identifies and counts occurrences of common suspicious string patterns within a given text file, using regular expressions.

## Install
```
git clone https://github.com/ShadowGuard-AI/analyze-string-patterns
cd analyze-string-patterns
pip install -r requirements.txt
```

## Usage
```
python3 main.py FILEPATH [-o OUTPUT] [-l LEVEL]
```

## Parameters
- `FILEPATH`: path to the text file to analyze.
- `-h`: show help message and exit.
- `-o`, `--output`: path to save the analysis results as a CSV file (optional).
- `-l`, `--log_level`: logging level: `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`. Default: `INFO`.

## Verified behavior
- A sample containing one IP address, one email address, and one URL reported a count of 1 for each of those three patterns and 0 for Hex Encoded, MD5 Hash, SHA1 Hash, SHA256 Hash, and Base64 Encoded.
- With `-o`, the CSV has two columns, `Pattern` and `Count`.
- A missing input file exits 1.

## License
MIT License, see LICENSE.
