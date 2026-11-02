![The coast in fog: black rock with a rope coil and a crate in the foreground, the bell tower alone on its headland, the hut unlit behind it, layered fog banks above, nothing readable](intro-banner.png)

# analyze-string-patterns

![A headland station in fog, the bell swinging a short arc, one apricot window lit in the hut, the name painted in cirrus white along the hut wall and worn at the ends, the only lettering on the coast](banner.png)

![A fog bell in a squat open tower cut in half by a hard fog line, one post carrying a narrow altitude blue band, the heading plate](logo.png)

![Coast scene in three layers of obscurity: fog drifts across the near rock and crate, the bell swings in a short arc at uneven intervals and rests, and the far headland gains and loses definition and vanishes once completely in a long cycle](scene.svg)


# analyze-string-patterns
Identifies and counts occurrences of common suspicious string patterns within a given text file, using regular expressions.


![Minor section divider: a smaller thunderhead centred on a silver rule, no flicker](sep-light.svg)

## Install
```
git clone https://github.com/ShadowGuard-AI/analyze-string-patterns
cd analyze-string-patterns
pip install -r requirements.txt
```


![Major section divider: a small thunderhead on a silver rule, with a single flicker inside](sep-heavy.svg)

## Usage
```
python3 main.py FILEPATH [-o OUTPUT] [-l LEVEL]
```


![Minor section divider: a smaller thunderhead centred on a silver rule, no flicker](sep-light.svg)

## Parameters
- `FILEPATH`: path to the text file to analyze.
- `-h`: show help message and exit.
- `-o`, `--output`: path to save the analysis results as a CSV file (optional).
- `-l`, `--log_level`: logging level: `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`. Default: `INFO`.


![Major section divider: a small thunderhead on a silver rule, with a single flicker inside](sep-heavy.svg)

## Verified behavior
- A sample containing one IP address, one email address, and one URL reported a count of 1 for each of those three patterns and 0 for Hex Encoded, MD5 Hash, SHA1 Hash, SHA256 Hash, and Base64 Encoded.

> Keeper's note: the verified sample counts stand as tested evidence, three patterns found once each and five not found at all in the sample that was run. The tally is one sample result, not a promise about other files.
- With `-o`, the CSV has two columns, `Pattern` and `Count`.
- A missing input file exits 1.

> Keeper's note: a missing input file exits 1. That is the failure condition a reader planning a run needs to trust before relying on the output.


![Major section divider: a small thunderhead on a silver rule, with a single flicker inside](sep-heavy.svg)

## License
MIT License, see LICENSE.
