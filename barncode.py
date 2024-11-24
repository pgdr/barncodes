from io import BytesIO

from barcode import EAN13
from barcode.writer import SVGWriter

import sys

key = sys.argv[1]
assert 0 < int(key) < 10**5

with open(f"{key}.svg", "wb") as f:
    EAN13(f"70000000{key}", writer=SVGWriter()).write(f)
