# JRC-TMF-CD256 v2.0

JRC-TMF-CD256 v2.0 is a 256x256 forest change detection benchmark release candidate derived from JRC Tropical Moist Forest / Landsat-based Google Earth Engine exports. The fixed temporal pair is 2020 -> 2023.

## Dataset identity

- Name: JRC-TMF-CD256
- Version: v2.0 release candidate
- Task: binary forest change detection with ignore mask
- Patch size: 256x256
- Time pair: 2020 -> 2023
- Samples: 5000
- Positive / negative: 3682 / 1318
- Regions: Amazon, Congo Basin, Southeast Asia
- ROI/export regions: 19

## Directory layout

- `data/JRC_TMF_256_5000/A`: time-1 image patches.
- `data/JRC_TMF_256_5000/B`: time-2 image patches.
- `data/JRC_TMF_256_5000/label`: labels with values 0, 1, and 255.
- `data/JRC_TMF_256_5000/metadata.csv`: per-sample metadata and quality-control fields.
- `data/JRC_TMF_256_5000/splits`: fixed train/val/test split files.
- `quality_report`: automated checks, reliability outputs, and human-audit contact sheets.
- `docs`: ROI table, metadata schema, audit forms, audit guide, baseline plan, and release checklist.
- `scripts`: reproducibility and post-audit utility scripts.

## v2.0 statistics

- Triplets: 5000
- Positive / negative: 3682 / 1318
- Train / val / test: 4005 / 500 / 495
- Valid ratio: min 0.800003, mean 0.967896, median 0.992523
- Change ratio: min 0.000000, mean 0.012590, median 0.004890, max 0.453131
- Label values: 0 no-change, 1 change, 255 ignore

## Quality controls completed

- A/B/label triplet count consistency.
- Label value check restricted to [0, 1, 255].
- Valid-ratio filtering with selected samples satisfying valid_ratio >= 0.80.
- Positive/negative sample accounting.
- Fixed train/val/test split generation.
- Split leakage check.
- Exact duplicate triplet/image check.
- 300-sample stratified human-audit package generated.

## Pending before public DOI release

- Human audit results expected 2026-05-06.
- Baseline model experiments and final result table.
- Final license wording after confirming upstream JRC TMF, Landsat, and Google Earth Engine requirements.
- DOI/platform publication step, if approved by the dataset owner.

## Recommended citation note

Before public release, add the final DOI citation and the required upstream data citations for JRC Tropical Moist Forest, Landsat data products, and Google Earth Engine processing.
