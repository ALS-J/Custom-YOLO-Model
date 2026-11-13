#Please read and follow the README.md file first
import random
import shutil
from pathlib import Path

SRC = Path(r"") #Directory where your label-studio export is placed
DST = Path(r"") #Directory where your label-studio export is placed

Ratio = 0.2
random.seed(42)

images = [p for p in (SRC / "images").iterdir()
          if p.suffix.lower() in {".jpg", ".jpeg", ".png"}]
random.shuffle(images)

n_val = max(1, int(len(images) * Ratio))
splits = {"val": images[:n_val], "train": images[n_val:]}

for split, files in splits.items():
    (DST / "images" / split).mkdir(parents=True, exist_ok=True)
    (DST / "labels" / split).mkdir(parents=True, exist_ok=True)
    for img in files:
        label = SRC / "labels" / (img.stem + ".txt")
        shutil.copy2(img, DST / "images" / split / img.name)
        if label.exists():
            shutil.copy2(label, DST / "labels" / split / label.name)

print({k: len(v) for k, v in splits.items()})