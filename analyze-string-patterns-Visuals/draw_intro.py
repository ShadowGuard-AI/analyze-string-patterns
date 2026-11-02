#!/usr/bin/env python3
"""analyze-string-patterns intro: the coast in fog, nothing written anywhere. Foreground: black rock at
the bottom of the frame, wet at its lower edge, a coil of rope and a wooden crate resting on it in soft
focus, fog already curling round the crate corners. Midground: the bell tower alone on its headland, bell
at rest, the keeper's hut behind it unlit and shuttered, a path that starts toward the tower and loses
itself in white before it arrives. Background: stacked banks of fog in cirrus white and silver reaching
to the top of the frame, the farther headland barely a change of tone on the right, and dawn apricot
lightening the highest bank without breaking through anywhere. The bell does not move in this view."""
import random, sys
from PIL import Image, ImageDraw, ImageFilter
random.seed(61)
A = sys.argv[1] if len(sys.argv) > 1 else ""
W, H = 1200, 520
BLUE = (58, 95, 138); SILVER = (192, 196, 200); CIRRUS = (242, 243, 240); APRICOT = (232, 165, 107)
img = Image.new("RGB", (W, H), SILVER); d = ImageDraw.Draw(img, "RGBA")
# stacked banks of fog reaching to the top of the frame, apricot lightening the highest bank only
for i, (y0, y1, col, a) in enumerate([(0, 92, (234, 224, 208), 255), (90, 210, CIRRUS, 235), (180, 300, (214, 218, 220), 225), (270, 380, CIRRUS, 215), (350, 460, (206, 210, 214), 205)]):
    d.polygon([(0, y0), (W, y0), (W, y1), (0, y1 + 26)], fill=(col[0], col[1], col[2], a))
for _ in range(46):  # soft bank edges
    x, y = random.uniform(0, W), random.choice([96, 190, 282, 366, 448])
    r = random.uniform(30, 90)
    d.ellipse([x - r, y - r * 0.32, x + r, y + r * 0.32], fill=(242, 243, 240, 60))
# the farther headland: barely a change of tone on the right
d.polygon([(880, 380), (1010, 300), (1130, 322), (1200, 352), (1200, 420), (880, 420)], fill=(168, 174, 180, 130))
d.rectangle([1052, 268, 1058, 302], fill=(150, 156, 162, 110))  # its tower reduced to a vertical smudge
# the near headland and the path that loses itself in white before it arrives
d.polygon([(0, 520), (0, 402), (240, 366), (520, 378), (700, 420), (760, 520)], fill=(96, 102, 108))
d.polygon([(120, 520), (300, 420), (368, 402), (392, 416), (300, 520)], fill=(226, 228, 226, 120))  # the path, whitening as it goes
for a_, y_ in [(150, 428), (200, 452), (235, 478)]:
    d.line([(0, y_), (760, y_ + 30)], fill=(242, 243, 240, a_), width=15)  # fog closing over the path
# the keeper's hut behind the tower, unlit and shuttered
hx, hy = 452, 330
d.rectangle([hx, hy, hx + 148, hy + 74], fill=(74, 78, 84))
d.polygon([(hx - 10, hy), (hx + 74, hy - 34), (hx + 158, hy)], fill=(52, 56, 62))
d.rectangle([hx + 22, hy + 22, hx + 52, hy + 52], fill=(60, 64, 70), outline=(40, 44, 50), width=2)  # shuttered window, dark
d.line([(hx + 37, hy + 22), (hx + 37, hy + 52)], fill=(40, 44, 50), width=2)
if A == "--v2":  # v2 flaw: the hut window lit apricot in a view the prose keeps unlit
    d.rectangle([hx + 24, hy + 24, hx + 50, hy + 50], fill=APRICOT)
# the bell tower alone on its headland: two short posts, a timber crossbeam, a heavy bell at rest
tx, ty = 300, 402
for px_ in (tx - 52, tx + 44):
    d.rectangle([px_, ty - 148, px_ + 9, ty], fill=(44, 46, 50))
d.rectangle([tx - 66, ty - 160, tx + 68, ty - 146], fill=(50, 48, 46))  # crossbeam
d.polygon([(tx - 72, ty - 160), (tx, ty - 188), (tx + 74, ty - 160)], fill=(58, 60, 64))  # low cap roof, not a steeple
if A == "--v1":  # v1 flaw: a spire raised over the bell, a church steeple on a fog station
    d.polygon([(tx - 20, ty - 188), (tx, ty - 246), (tx + 22, ty - 188)], fill=(58, 60, 64))
    d.line([(tx, ty - 246), (tx, ty - 262)], fill=(44, 46, 50), width=3)
# bell: silver, blue grey at the shoulder, mouth wide, clapper a dark shape inside the rim, at rest
d.polygon([(tx - 13, ty - 146), (tx + 13, ty - 146), (tx + 17, ty - 128), (tx + 26, ty - 104), (tx + 30, ty - 96), (tx - 30, ty - 96), (tx - 26, ty - 104), (tx - 17, ty - 128)], fill=(176, 184, 194))
d.polygon([(tx - 13, ty - 146), (tx + 13, ty - 146), (tx + 17, ty - 128), (tx - 17, ty - 128)], fill=(110, 132, 158))  # blue grey shoulder
d.ellipse([tx - 30, ty - 102, tx + 30, ty - 90], fill=(206, 210, 214))
d.ellipse([tx - 7, ty - 104, tx + 7, ty - 86], fill=(30, 32, 36))  # the clapper inside the rim
# foreground: black rock at the bottom, wet at its lower edge
rock = Image.new("RGBA", (W, H), (0, 0, 0, 0)); rd = ImageDraw.Draw(rock)
rd.polygon([(0, 520), (0, 452), (260, 432), (620, 446), (960, 436), (1200, 458), (1200, 520)], fill=(16, 17, 20, 255))
rd.line([(0, 508), (1200, 500)], fill=(120, 134, 148, 130), width=3)  # the wet lower edge catching light
# a coil of rope and a wooden crate on the rock, soft focus, fog curling round the crate corners
rd.ellipse([838, 452, 928, 478], outline=(104, 92, 74, 255), width=6)
rd.ellipse([856, 458, 912, 476], outline=(104, 92, 74, 255), width=5)
rd.rectangle([972, 428, 1052, 478], fill=(96, 78, 58, 255), outline=(64, 50, 36, 255), width=3)
rd.line([(972, 452), (1052, 452)], fill=(64, 50, 36, 200), width=3)
rd.line([(1012, 428), (1012, 478)], fill=(64, 50, 36, 200), width=3)
rock = rock.filter(ImageFilter.GaussianBlur(1.8 if A != "--v2" else 0.2))  # v2 also keeps the crate razor sharp and dominant
img.paste(Image.alpha_composite(img.convert("RGBA"), rock).convert("RGB"), (0, 0))
d = ImageDraw.Draw(img, "RGBA")
for (x, y, r) in [(962, 424, 34), (1058, 430, 28), (1006, 470, 40)]:  # fog curling round the crate corners
    d.ellipse([x - r, y - r * 0.36, x + r, y + r * 0.36], fill=(242, 243, 240, 120))
img = img.filter(ImageFilter.GaussianBlur(0.8))
out = {"--v1": "scratch/intro-v1.png", "--v2": "scratch/intro-v2.png"}.get(A, "intro-banner.png")
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)
