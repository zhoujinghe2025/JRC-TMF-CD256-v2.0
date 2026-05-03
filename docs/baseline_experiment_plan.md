# Baseline experiment plan for JRC-TMF-CD256 v2.0

## Goal

Provide reproducible baseline performance on the fixed JRC-TMF-CD256 v2.0 splits. Baseline results should be reported only after the human audit is incorporated into the final release candidate.

## Required split policy

- Use `data/JRC_TMF_256_5000/splits/train.txt` for training.
- Use `data/JRC_TMF_256_5000/splits/val.txt` for validation and model selection.
- Use `data/JRC_TMF_256_5000/splits/test.txt` once for final reporting.
- Do not mix train/val/test samples.
- Do not tune hyperparameters on the test split.

## Recommended baselines

| family | model | role |
|---|---|---|
| early-fusion CNN | FC-EF | classic low-complexity baseline |
| Siamese CNN | FC-Siam-conc | classic bi-temporal baseline |
| transformer/hybrid | BIT | widely used change-detection baseline |
| transformer | ChangeFormer | stronger transformer baseline |
| attention/CNN | MANet | modern segmentation-style baseline |
| proposed/local | Eagle-FNO | project method baseline |

## Required metrics

Report all metrics on valid pixels only, excluding label 255:

- Precision
- Recall
- F1
- IoU
- OA
- False positive rate, optional
- False negative rate, optional

## Reporting requirements

For each model, record:

- model name
- code source or commit
- random seed
- input normalization
- augmentations
- optimizer
- learning rate
- batch size
- epoch count
- selected checkpoint criterion
- GPU/CPU environment
- train/val/test split identifiers
- test metrics

## Output files

Use `docs/baseline_results_template.csv` for the final table. Store detailed logs under a future `baseline_results/` directory if experiments are run locally.

## Notes before running

Baseline experiments should wait until human audit outcomes are integrated. If reject samples are removed or replaced, the final split files and checksums must be regenerated before training.
