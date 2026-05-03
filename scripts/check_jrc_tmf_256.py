"""Check JRC_TMF_256 dataset structure and label quality."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))

    from gfc_forest_256_builder.check_gfc_forest_256 import main as gfc_check_main

    if "--root" not in sys.argv:
        sys.argv.extend(["--root", str(repo_root / "JRC_TMF_256")])

    gfc_check_main()


if __name__ == "__main__":
    main()
