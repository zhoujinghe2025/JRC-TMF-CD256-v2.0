# GFC_Forest_256 Dataset Reliability Report

## Dataset Integrity
- Matched triplets: 5000
- A/B/label counts: 5000 / 5000 / 5000
- Bad shape count: 0
- Bad label value count: 0

## Fixed Splits
- Train / Val / Test: 4005 / 500 / 495
- Split intersections: {'train_val': 0, 'test_train': 0, 'test_val': 0}
- Exact triplet duplicate groups: 0
- Exact A+B image duplicate groups: 0
- Cross-split near-duplicate examples recorded: 0

## Label Distribution
- Valid pixel ratio: 0.967896
- Change pixel ratio among valid pixels: 0.012139
- Source counts: {'jrc_tmf_2020_2023_amazon_bolivia_01': 154, 'jrc_tmf_2020_2023_amazon_brazil_01': 243, 'jrc_tmf_2020_2023_amazon_brazil_02_stable': 267, 'jrc_tmf_2020_2023_amazon_colombia_01': 217, 'jrc_tmf_2020_2023_amazon_colombia_02_stable': 280, 'jrc_tmf_2020_2023_amazon_guyana_01_stable': 96, 'jrc_tmf_2020_2023_amazon_peru_01': 365, 'jrc_tmf_2020_2023_amazon_peru_02_stable': 272, 'jrc_tmf_2020_2023_congo_cameroon_01': 389, 'jrc_tmf_2020_2023_congo_drc_01': 355, 'jrc_tmf_2020_2023_congo_drc_02_stable': 415, 'jrc_tmf_2020_2023_congo_gabon_01': 266, 'jrc_tmf_2020_2023_congo_gabon_02_stable': 268, 'jrc_tmf_2020_2023_congo_roc_01_stable': 183, 'jrc_tmf_2020_2023_se_asia_borneo_01': 390, 'jrc_tmf_2020_2023_se_asia_borneo_02_stable': 279, 'jrc_tmf_2020_2023_se_asia_papua_01_stable': 318, 'jrc_tmf_2020_2023_se_asia_sumatra_01': 105, 'jrc_tmf_2020_2023_se_asia_sumatra_02_stable': 138}
- Split source counts: {'train': {'jrc_tmf_2020_2023_amazon_bolivia_01': 132, 'jrc_tmf_2020_2023_amazon_brazil_01': 186, 'jrc_tmf_2020_2023_amazon_brazil_02_stable': 188, 'jrc_tmf_2020_2023_amazon_colombia_01': 189, 'jrc_tmf_2020_2023_amazon_colombia_02_stable': 238, 'jrc_tmf_2020_2023_amazon_guyana_01_stable': 61, 'jrc_tmf_2020_2023_amazon_peru_01': 278, 'jrc_tmf_2020_2023_amazon_peru_02_stable': 239, 'jrc_tmf_2020_2023_congo_cameroon_01': 321, 'jrc_tmf_2020_2023_congo_drc_01': 319, 'jrc_tmf_2020_2023_congo_drc_02_stable': 366, 'jrc_tmf_2020_2023_congo_gabon_01': 208, 'jrc_tmf_2020_2023_congo_gabon_02_stable': 206, 'jrc_tmf_2020_2023_congo_roc_01_stable': 146, 'jrc_tmf_2020_2023_se_asia_borneo_01': 304, 'jrc_tmf_2020_2023_se_asia_borneo_02_stable': 210, 'jrc_tmf_2020_2023_se_asia_papua_01_stable': 242, 'jrc_tmf_2020_2023_se_asia_sumatra_01': 83, 'jrc_tmf_2020_2023_se_asia_sumatra_02_stable': 89}, 'val': {'jrc_tmf_2020_2023_amazon_bolivia_01': 13, 'jrc_tmf_2020_2023_amazon_brazil_01': 24, 'jrc_tmf_2020_2023_amazon_brazil_02_stable': 30, 'jrc_tmf_2020_2023_amazon_colombia_01': 16, 'jrc_tmf_2020_2023_amazon_colombia_02_stable': 23, 'jrc_tmf_2020_2023_amazon_guyana_01_stable': 11, 'jrc_tmf_2020_2023_amazon_peru_01': 45, 'jrc_tmf_2020_2023_amazon_peru_02_stable': 15, 'jrc_tmf_2020_2023_congo_cameroon_01': 21, 'jrc_tmf_2020_2023_congo_drc_01': 23, 'jrc_tmf_2020_2023_congo_drc_02_stable': 36, 'jrc_tmf_2020_2023_congo_gabon_01': 37, 'jrc_tmf_2020_2023_congo_gabon_02_stable': 30, 'jrc_tmf_2020_2023_congo_roc_01_stable': 16, 'jrc_tmf_2020_2023_se_asia_borneo_01': 32, 'jrc_tmf_2020_2023_se_asia_borneo_02_stable': 47, 'jrc_tmf_2020_2023_se_asia_papua_01_stable': 52, 'jrc_tmf_2020_2023_se_asia_sumatra_01': 11, 'jrc_tmf_2020_2023_se_asia_sumatra_02_stable': 18}, 'test': {'jrc_tmf_2020_2023_amazon_bolivia_01': 9, 'jrc_tmf_2020_2023_amazon_brazil_01': 33, 'jrc_tmf_2020_2023_amazon_brazil_02_stable': 49, 'jrc_tmf_2020_2023_amazon_colombia_01': 12, 'jrc_tmf_2020_2023_amazon_colombia_02_stable': 19, 'jrc_tmf_2020_2023_amazon_guyana_01_stable': 24, 'jrc_tmf_2020_2023_amazon_peru_01': 42, 'jrc_tmf_2020_2023_amazon_peru_02_stable': 18, 'jrc_tmf_2020_2023_congo_cameroon_01': 47, 'jrc_tmf_2020_2023_congo_drc_01': 13, 'jrc_tmf_2020_2023_congo_drc_02_stable': 13, 'jrc_tmf_2020_2023_congo_gabon_01': 21, 'jrc_tmf_2020_2023_congo_gabon_02_stable': 32, 'jrc_tmf_2020_2023_congo_roc_01_stable': 21, 'jrc_tmf_2020_2023_se_asia_borneo_01': 54, 'jrc_tmf_2020_2023_se_asia_borneo_02_stable': 22, 'jrc_tmf_2020_2023_se_asia_papua_01_stable': 24, 'jrc_tmf_2020_2023_se_asia_sumatra_01': 11, 'jrc_tmf_2020_2023_se_asia_sumatra_02_stable': 31}}

## Image Quality Proxy
- Phase-correlation samples: 200
- Phase-shift abs-pixel quantiles: {'min': 0.0, 'p05': 0.0, 'p25': 0.0, 'median': 0.0, 'p75': 0.0, 'p95': 22.08884152126083, 'max': 33.61547262794322, 'mean': 1.8532726181021908, 'std': 6.647584569074142}

## Human Verification Files
- `human_double_annotation_samples.csv`: samples for two independent annotators.
- `human_quality_audit_samples.csv`: samples for manual quality audit.

## Suggested Paper Statement
We provide a fixed spatial-block split and report file-level, hash-level, and perceptual-hash leakage checks. Dataset statistics include source distribution, valid-pixel ratio, change-pixel ratio, and per-sample change-area distribution. A stratified subset is reserved for independent double annotation and manual quality auditing.
