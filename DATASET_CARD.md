# Dataset Card: JRC-TMF-CD256 v2.0

## Dataset identity

- Dataset name: JRC-TMF-CD256
- Version: v2.0 release candidate
- Task: binary forest change detection
- Spatial size: 256x256 pixels
- Temporal pair: 2020 -> 2023
- Number of triplets: 5000
- Positive / negative: 3682 / 1318
- Splits: train 4005, val 500, test 495
- Label values: 0 no-change, 1 change, 255 ignore

## Intended use

This dataset is intended for supervised remote-sensing forest change detection benchmarking under fixed train/validation/test splits. It is suitable for model comparison, ablation studies, and reproducibility-oriented experiments on tropical forest change detection.

## Not intended use

The dataset should not be used as a standalone operational deforestation monitoring product, legal evidence of land-cover change, or a substitute for official forest monitoring systems. It is a benchmark dataset derived from upstream products and carries their limitations.

## Data sources and derivation

The samples are derived from JRC Tropical Moist Forest / Landsat-based Google Earth Engine exports. The v2.0 package includes 19 ROI/export regions covering Amazon, Congo Basin, and Southeast Asia. The fixed time pair is 2020 -> 2023. Patches are selected as 256x256 triplets containing A image, B image, and label.

## Dataset composition

- A images: time-1 patches.
- B images: time-2 patches.
- Labels: binary change labels with ignore mask.
- Metadata: per-sample sample_id, sample_type, source ROI/export, source GeoTIFF path, x/y patch location, valid_ratio, change_ratio, change_pixels, and valid_pixels.
- Splits: fixed train/val/test text files.

## Quality-control summary

Automated checks report:

- A/B/label files: 5000 / 5000 / 5000.
- Label values restricted to [0, 1, 255].
- Bad shape count: 0 in the checked v2.0 candidate.
- Split leakage: 0 intersections among train, val, and test.
- Exact duplicate triplet/image count: 0 in the reliability check.
- valid_ratio min: 0.800003.
- valid_ratio mean: 0.967896.
- change_ratio mean: 0.012590.

## Human audit status

A stratified human-audit package has been generated with 300 contact sheets. Manual review results are expected on 2026-05-06. After review, the audit outcomes should be summarized and, if needed, reject samples should be removed or replaced before public release.

## Baseline status

Baseline experiments are pending. Recommended baselines include FC-EF, FC-Siam-conc, BIT, ChangeFormer, MANet, and Eagle-FNO. Report Precision, Recall, F1, IoU, and OA on the fixed test split.

## Known limitations

- Upstream classification artifacts may remain.
- Cloud, cloud shadow, water, smoke, haze, terrain shadow, seasonal effects, and non-forest disturbances may affect difficult samples.
- The dataset is spatially broader than a single-site benchmark, but it is still limited to selected ROI/export regions.
- Labels are derived from upstream products rather than fresh manual pixel-level annotation.
- Final publication should wait for completed manual audit and baseline results.

## Licensing and attribution

This local release candidate is derived from upstream JRC Tropical Moist Forest / Landsat / Google Earth Engine workflows. Public release requires final license wording consistent with all upstream data-use terms and attribution requirements.
