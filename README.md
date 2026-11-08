![Hands close up working a wooden mending needle along one row of the net, the finished knots even behind the needle and the red float resting beside the work](intro-banner.png)

# analyze-string-patterns

![Long fishing net spread across a harbour quay to dry, its knot rows running the length of the frame, cork floats along the near edge with one red float among them, a mending bench with a ball of twine at the left edge and the harbour still behind](banner.png)

![Section of fishing net from directly above spread flat on a stone quay, even rows of hemp knots across the frame and a line of round cork floats along one edge with one single red float among the corks](logo.png)

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
