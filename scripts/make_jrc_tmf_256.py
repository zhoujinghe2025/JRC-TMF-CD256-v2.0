"""Build JRC_TMF_256 patches from exported GeoTIFF files.

The GeoTIFF band contract is identical to the GFC builder:

  A_R, A_G, A_B, B_R, B_G, B_B, label

This wrapper reuses the tested GFC tiling implementation and pins JRC/TMF
defaults that protect training quality:

- valid_min=0.80 keeps patches with enough non-ignore label area.
- neg_ratio=2.0 prefers negative samples whenever enough candidates exist.
"""

from __future__ import annotations

import sys
from pathlib import Path


def add_default(flag: str, value: str) -> None:
    if flag not in sys.argv:
        sys.argv.extend([flag, value])


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))

    from gfc_forest_256_builder.make_gfc_forest_256 import main as gfc_main

    add_default("--out", str(repo_root / "JRC_TMF_256"))
    add_default("--valid-min", "0.80")
    add_default("--pos-min", "0.002")
    add_default("--neg-ratio", "2.0")

    gfc_main()


if __name__ == "__main__":
    main()
