#!/usr/bin/env python3
"""analyze-string-patterns wordmark banner: a headland station on a grey morning when the sea has vanished
into its own weather. In the middle distance the fog bell tower stands on black rock, bell swinging a
short arc, and beside it a low keeper's hut with one window lit in dawn apricot, the sole warm light on
the coast. A second headland shows as a paler shape far to the right, its own bell tower reduced to a
vertical smudge, and between the two headlands the fog lies in layered banks of cirrus white and silver
with no water visible beneath them. Gulls sit motionless on the tower roof and on the hut ridge, heads
tucked. The project name is painted in BBH Bogle in cirrus white along the hut's long wall, weather worn
at the ends, and it is the only lettering on the coast."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(17)
A = sys.argv[1] if len(sys.argv) > 1 else ""
W, H = 1200, 420
BLUE = (58, 95, 138); SILVER = (192, 196, 200); CIRRUS = (242, 243, 240); APRICOT = (232, 165, 107)
img = Image.new("RGB", (W, H), SILVER); d = ImageDraw.Draw(img, "RGBA")
# layered banks of fog, cirrus white and silver, no water visible beneath them
for (y0, y1, col, a) in [(0, 80, (233, 223, 207), 255), (70, 168, CIRRUS, 235), (140, 238, (212, 216, 219), 228), (210, 300, CIRRUS, 218), (272, 348, (204, 208, 212), 210)]:
    d.polygon([(0, y0), (W, y0), (W, y1), (0, y1 + 20)], fill=(col[0], col[1], col[2], a))
for _ in range(38):
    x, y = random.uniform(0, W), random.choice([84, 156, 226, 288, 336])
    r = random.uniform(28, 84)
    d.ellipse([x - r, y - r * 0.3, x + r, y + r * 0.3], fill=(242, 243, 240, 55))
# the second headland far to the right, a paler shape, its tower a vertical smudge
d.polygon([(930, 348), (1030, 276), (1146, 292), (1200, 318), (1200, 372), (930, 372)], fill=(164, 170, 176, 150))
d.rectangle([1078, 240, 1085, 280], fill=(148, 154, 160, 130))
# the near headland: black rock
d.polygon([(0, 420), (0, 330), (220, 302), (560, 310), (760, 344), (820, 420)], fill=(88, 94, 100))
d.polygon([(0, 420), (0, 366), (300, 344), (640, 356), (820, 420)], fill=(20, 21, 24))
# the keeper's hut beside the tower, one window lit in dawn apricot
hx, hy = 430, 252
d.rectangle([hx, hy, hx + 300, hy + 92], fill=(70, 74, 80))
d.polygon([(hx - 12, hy), (hx + 150, hy - 38), (hx + 312, hy)], fill=(48, 51, 56))
d.rectangle([hx + 236, hy + 26, hx + 268, hy + 58], fill=APRICOT)  # the sole warm light on the coast
d.rectangle([hx + 236, hy + 26, hx + 268, hy + 58], outline=(120, 84, 50), width=2)
d.line([(hx + 252, hy + 26), (hx + 252, hy + 58)], fill=(120, 84, 50), width=2)
try:
    f = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/BBHBogle.ttf", 25)
except Exception:
    f = ImageFont.load_default()
name = "analyze-string-patterns"
if A == "--v1":  # v1 flaw: the name on a board planted by the path, signage a working station does not carry
    d.rectangle([856, 268, 1150, 306], fill=(48, 51, 56), outline=(30, 32, 36), width=2)
    d.rectangle([996, 306, 1008, 348], fill=(30, 32, 36))
    d.text((1003, 287), name, font=f, fill=CIRRUS, anchor="mm")
elif A == "--v2":  # v2 flaw: the name painted full strength and unworn, fresh paint on a weather coast, and the gulls put in flight
    d.text((hx + 14, hy + 46), name, font=f, fill=(255, 255, 255), anchor="lm")
    for (gx, gy) in [(180, 90), (300, 66), (520, 100)]:
        d.arc([gx - 13, gy - 6, gx, gy + 6], 200, 330, fill=(52, 56, 62), width=2)
        d.arc([gx, gy - 6, gx + 13, gy + 6], 210, 340, fill=(52, 56, 62), width=2)
else:
    # painted along the hut's long wall in cirrus white, weather worn at the ends
    d.text((hx + 14, hy + 34), "analyze-string-", font=f, fill=(232, 234, 232, 225), anchor="lm")
    d.text((hx + 14, hy + 62), "patterns", font=f, fill=(232, 234, 232, 225), anchor="lm")
    for _ in range(26):  # wear eating the paint, heavier at the ends of the line
        x = random.choice([random.uniform(hx + 14, hx + 60), random.uniform(hx + 150, hx + 196)])
        y = random.choice([random.uniform(hy + 24, hy + 42), random.uniform(hy + 52, hy + 70)])
        d.line([(x, y), (x + random.uniform(3, 10), y)], fill=(70, 74, 80), width=2)
# the fog bell tower on the black rock, bell swinging a short arc (drawn mid swing, tilted)
tx, ty = 268, 344
for px_ in (tx - 50, tx + 42):
    d.rectangle([px_, ty - 140, px_ + 9, ty], fill=(40, 42, 46))
d.rectangle([tx - 64, ty - 152, tx + 66, ty - 138], fill=(48, 46, 44))
d.polygon([(tx - 70, ty - 152), (tx, ty - 180), (tx + 72, ty - 152)], fill=(54, 56, 60))  # tower roof
ang = math.radians(9)
bx, by = tx + math.sin(ang) * 8, ty - 138
d.polygon([(bx - 12, by), (bx + 12, by), (bx + 16 + 3, by + 24), (bx + 24 + 3, by + 44), (bx + 27 + 3, by + 52), (bx - 27 + 3, by + 52), (bx - 24 + 3, by + 44), (bx - 16 + 3, by + 24)], fill=(178, 186, 196))
d.polygon([(bx - 12, by), (bx + 12, by), (bx + 16 + 3, by + 24), (bx - 16 + 3, by + 24)], fill=(110, 132, 158))
d.ellipse([bx - 24, by + 46, bx + 30, by + 58], fill=(208, 211, 214))
d.ellipse([bx + 0, by + 46, bx + 13, by + 64], fill=(30, 32, 36))  # clapper swung with the bell
# gulls sitting motionless on the tower roof and on the hut ridge, heads tucked, waiting the murk out
def gull(x, y, s=1.0):
    d.ellipse([x - 11 * s, y - 6 * s, x + 11 * s, y + 5 * s], fill=(208, 212, 216), outline=(110, 116, 122))
    d.ellipse([x + 6 * s, y - 9 * s, x + 13 * s, y - 2 * s], fill=(214, 216, 218))  # head tucked against the body
    d.line([(x - 2 * s, y + 5 * s), (x - 2 * s, y + 9 * s)], fill=(90, 80, 60), width=2)
    d.line([(x + 4 * s, y + 5 * s), (x + 4 * s, y + 9 * s)], fill=(90, 80, 60), width=2)
if A != "--v2":
    gull(tx - 30, ty - 160); gull(tx + 34, ty - 156, 0.9); gull(hx + 104, hy - 28); gull(hx + 198, hy - 24, 0.92)
img = img.filter(ImageFilter.GaussianBlur(0.4))
out = {"--v1": "scratch/banner-v1.png", "--v2": "scratch/banner-v2.png"}.get(A, "banner.png")
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)
