from __future__ import annotations

from pathlib import Path
import random
import sys
from typing import Tuple
from PIL import Image, Image as PILImage
import colorsys


def random_hsv_color() -> Tuple[int, int, int]:
    """Return a random RGB color based on HSV where H is random, S=0.5 and V=0.5."""
    h: float = random.random()
    s: float = 0.5
    v: float = 0.5
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return int(r * 255), int(g * 255), int(b * 255)


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python main.py <input_dir> <output_dir>")
        sys.exit(1)

    input_directory: Path = Path(sys.argv[1])
    output_directory: Path = Path(sys.argv[2])
    output_directory.mkdir(parents=True, exist_ok=True)

    for in_path in input_directory.glob("*.png"):
        out_path: Path = output_directory / in_path.name

        with Image.open(in_path).convert("RGBA") as img:
            img: PILImage.Image
            w: int
            h: int
            w, h = img.size

            bg_color: Tuple[int, int, int] = random_hsv_color()
            bg: PILImage.Image = Image.new("RGBA", (w, h), bg_color + (255,))
            blended: PILImage.Image = Image.alpha_composite(bg, img)
            blended.convert("RGB").save(out_path)

        print("Processed", in_path.name)


if __name__ == "__main__":
    main()