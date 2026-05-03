"""Run local reliability checks for JRC_TMF_256.

This wraps the generic GFC reliability checker with JRC/TMF defaults, so the
JRC dataset can be rechecked offline after new GeoTIFF exports are added.
"""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))

    from dataset_reliability.run_gfc_reliability_checks import main as gfc_main

    if "--root" not in sys.argv:
        sys.argv.extend(["--root", str(repo_root / "JRC_TMF_256")])
    if "--out-dir" not in sys.argv:
        sys.argv.extend(["--out-dir", str(repo_root / "dataset_reliability_outputs" / "jrc_tmf_256")])

    gfc_main()


if __name__ == "__main__":
    main()
