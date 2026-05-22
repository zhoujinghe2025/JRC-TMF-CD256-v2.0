# JRC-TMF-CD256 v2.0-clean

JRC-TMF-CD256 is a 256x256 forest change detection benchmark derived from JRC Tropical Moist Forest / Landsat-based Google Earth Engine exports. The fixed temporal pair is 2020 -> 2023.

## Current public package

The current recommended package is **JRC-TMF-CD256 v2.0-clean**.

Download page:

https://github.com/zhoujinghe2025/JRC-TMF-CD256-v2.0/releases/tag/v2.0-clean

Direct dataset asset:

https://github.com/zhoujinghe2025/JRC-TMF-CD256-v2.0/releases/download/v2.0-clean/JRC-TMF-CD256-v2.0-clean.tar.gz

SHA256 checksum:

https://github.com/zhoujinghe2025/JRC-TMF-CD256-v2.0/releases/download/v2.0-clean/JRC-TMF-CD256-v2.0-clean.tar.gz.sha256

## Ubuntu download

```bash
wget -O JRC-TMF-CD256-v2.0-clean.tar.gz \
  https://github.com/zhoujinghe2025/JRC-TMF-CD256-v2.0/releases/download/v2.0-clean/JRC-TMF-CD256-v2.0-clean.tar.gz

wget -O JRC-TMF-CD256-v2.0-clean.tar.gz.sha256 \
  https://github.com/zhoujinghe2025/JRC-TMF-CD256-v2.0/releases/download/v2.0-clean/JRC-TMF-CD256-v2.0-clean.tar.gz.sha256

sha256sum -c JRC-TMF-CD256-v2.0-clean.tar.gz.sha256

tar -xzf JRC-TMF-CD256-v2.0-clean.tar.gz
```

Expected SHA256:

```text
b52abe8ba9f9650b43a6b4351578b36f24bbd5d509abaec08e640ef2438e0e51
```

## Dataset identity

- Name: JRC-TMF-CD256
- Version: v2.0-clean release candidate
- Task: binary forest change detection with ignore mask
- Patch size: 256x256
- Time pair: 2020 -> 2023
- Samples: 5000 triplets
- Positive / negative: 3689 / 1311
- Regions: Amazon, Congo Basin, Southeast Asia
- ROI/export regions: 19

## Package contents

The release asset contains:

- `data/JRC_TMF_256_5000`: A/B/label patches, metadata, and fixed splits.
- `quality_report`: structure checks, reliability checks, clean-preparation report, and human-audit reports.
- `docs`: ROI table, audit tables, release notes, metadata schema, and publication materials.
- `scripts`: reproducibility and post-audit utility scripts.
- `README.md`, `DATASET_CARD.md`, `LICENSE`, `CITATION.cff`, `VERSION`, and `checksums.sha256`.

## Quality controls completed

- A/B/label triplet count consistency: 5000 / 5000 / 5000.
- Label value check restricted to `[0, 1, 255]`.
- Valid-ratio filtering with selected samples satisfying `valid_ratio >= 0.80`.
- Final positive / negative count: 3689 / 1311.
- Fixed train/val/test split generation.
- Split leakage check: no train/val/test overlap.
- Exact duplicate triplet/image check: no exact duplicates detected.
- Two-reviewer human audit plus adjudication completed for the sampled audit set.
- Final human audit summary: accept 231, flag 50, reject 19 among 300 audited samples.
- The 19 final-reject audited samples were removed and replaced before packaging `v2.0-clean`.

## Notes before DOI publication

This GitHub Release is the public dataset package for review and distribution. For a formal DOI release, the remaining recommended steps are baseline model experiments, final upstream license wording, and DOI minting through Zenodo/Figshare/Hugging Face Dataset or another approved repository.
