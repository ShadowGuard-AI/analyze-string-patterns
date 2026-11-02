#!/usr/bin/env python3
"""analyze-string-patterns logo: a fog bell in a squat open tower, drawn front on: a heavy bell in silver
hanging from a timber crossbeam between two short posts, its mouth wide and its clapper visible as a dark
shape inside the rim. Behind the posts a bank of fog in cirrus white cuts the scene in half horizontally,
so the tower rises out of nothing and the ground below the fog line is simply absent. One post carries a
narrow altitude blue band near its top, the only saturated colour in the mark, and the bell metal shades
from blue grey at the shoulder to silver at the lip. Under the fog line the name is set in BBH Bogle in
altitude blue on cirrus white."""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
A = sys.argv[1] if len(sys.argv) > 1 else ""
W, H = 900, 520
BLUE = (58, 95, 138); SILVER = (192, 196, 200); CIRRUS = (242, 243, 240)
img = Image.new("RGB", (W, H), CIRRUS); d = ImageDraw.Draw(img, "RGBA")
FOG = 300
# sky above the fog line: pale silver grey, empty
d.rectangle([0, 0, W, FOG], fill=(214, 218, 220))
d.polygon([(0, FOG - 26), (W, FOG - 44), (W, FOG), (0, FOG)], fill=CIRRUS)  # the hard horizontal fog edge
cx = 450
# two short posts and a timber crossbeam; the tower rises out of the fog, no ground below the line
for px_ in (cx - 118, cx + 104):
    d.rectangle([px_, 108, px_ + 15, FOG + 4], fill=(52, 52, 50))
d.rectangle([cx - 140, 92, cx + 142, 110], fill=(62, 56, 50))  # crossbeam
d.rectangle([cx - 140, 92, cx + 142, 97], fill=(84, 76, 66))
if A != "--v2":  # v2 flaw: the blue band painted on both posts, doubling the one saturated note
    pass
d.rectangle([cx - 118, 128, cx - 103, 142], fill=BLUE)  # the narrow altitude blue band on one post
if A == "--v2":
    d.rectangle([cx + 104, 128, cx + 119, 142], fill=BLUE)
if A == "--v1":  # v1 flaw: the bell given a handle and a rounded crown, a handbell on a stick
    d.rectangle([cx - 6, 44, cx + 6, 94], fill=(90, 70, 44))
    d.ellipse([cx - 34, 84, cx + 34, 118], fill=(168, 176, 186))
    d.polygon([(cx - 34, 100), (cx + 34, 100), (cx + 44, 168), (cx + 48, 178), (cx - 48, 178), (cx - 44, 168)], fill=(188, 194, 200))
    d.ellipse([cx - 48, 170, cx + 48, 186], fill=(210, 213, 216))
    d.ellipse([cx - 8, 172, cx + 8, 192], fill=(30, 32, 36))
else:
    # heavy bell: blue grey at the shoulder shading to silver at the lip, mouth wide, clapper inside
    d.rectangle([cx - 10, 110, cx + 10, 124], fill=(70, 74, 78))  # crown staple to the beam
    d.polygon([(cx - 30, 124), (cx + 30, 124), (cx + 40, 152), (cx + 58, 196), (cx + 66, 210), (cx - 66, 210), (cx - 58, 196), (cx - 40, 152)], fill=(186, 192, 198))
    d.polygon([(cx - 30, 124), (cx + 30, 124), (cx + 40, 152), (cx - 40, 152)], fill=(110, 132, 158))  # blue grey shoulder
    d.polygon([(cx - 58, 196), (cx + 58, 196), (cx + 66, 210), (cx - 66, 210)], fill=(216, 219, 222))  # silver at the lip
    d.ellipse([cx - 66, 202, cx + 66, 220], fill=(222, 225, 228))
    d.ellipse([cx - 13, 206, cx + 13, 234], fill=(30, 32, 36))  # the clapper, a dark shape inside the rim
try:
    fb = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/BBHBogle.ttf", 44)
    fr = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/Bitter.ttf", 38)
except Exception:
    fb = fr = ImageFont.load_default()
name = "analyze-string-patterns"
# under the fog line: cirrus white ground, the name in altitude blue (the fog band itself is the white field)
d.rectangle([0, FOG, W, H], fill=CIRRUS)
src = fr if A == "--v2" else fb
size = 44 if A != "--v2" else 38
while size > 12:
    trial = ImageFont.truetype(__file__.rsplit("/", 1)[0] + ("/fonts/Bitter.ttf" if A == "--v2" else "/fonts/BBHBogle.ttf"), size)
    if d.textlength(name, font=trial) <= 856:
        src = trial; break
    size -= 2
d.text((450, 408), name, font=src, fill=BLUE, anchor="mm")
img = img.filter(ImageFilter.GaussianBlur(0.3))
out = {"--v1": "scratch/logo-v1.png", "--v2": "scratch/logo-v2.png"}.get(A, "logo.png")
img.save(__file__.rsplit("/", 1)[0] + "/" + out)
if A == "":
    img.resize((64, 37)).save(__file__.rsplit("/", 1)[0] + "/scratch/logo64-ship.png")
print("saved", out)
