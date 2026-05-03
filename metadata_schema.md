# Metadata schema for JRC-TMF-CD256 v2.0

`data/JRC_TMF_256_5000/metadata.csv` contains one row per 256x256 A/B/label triplet.

## Core columns

| column | type | example | description |
|---|---|---|---|
| `sample_id` | string | `jrc_tmf_2020_2023_amazon_peru_01_005120_004608` | Unique sample identifier. Also matches the A/B/label PNG filename stem. |
| `sample_type` | categorical | `positive`, `negative` | Dataset balance category. Positive samples contain nonzero valid change pixels; negative samples contain no selected valid change pixels under the builder rule. |
| `source` | string | `jrc_tmf_2020_2023_amazon_peru_01` | Source ROI/export identifier. |
| `tif_path` | string | local path | Source GeoTIFF path used during local construction. For public release, this may be treated as provenance metadata rather than a portable path. |
| `x` | integer | `5120` | Pixel x-offset of the 256x256 crop in the source GeoTIFF stack. |
| `y` | integer | `4608` | Pixel y-offset of the 256x256 crop in the source GeoTIFF stack. |
| `valid_ratio` | float [0,1] | `0.9835` | Fraction of pixels not equal to ignore label 255. Selected v2.0 samples satisfy valid_ratio >= 0.80. |
| `change_ratio` | float [0,1] | `0.0052` | Fraction of valid pixels labeled as change. |
| `change_pixels` | integer | `333` | Count of valid pixels labeled 1. |
| `valid_pixels` | integer | `64456` | Count of non-ignore pixels. |

## Label values

| value | meaning |
|---:|---|
| 0 | valid no-change pixel |
| 1 | valid change pixel |
| 255 | ignore / invalid pixel |

## Split files

The split files are stored under `data/JRC_TMF_256_5000/splits/`:

- `train.txt`
- `val.txt`
- `test.txt`

Each line contains the PNG filename for one sample. The corresponding sample identifier is the filename without `.png`.

## Human-audit columns

Human-audit forms are stored separately under `docs/`. Audit columns include:

| column | allowed values | description |
|---|---|---|
| `audit_status` | `accept`, `flag`, `reject` | Final manual quality judgement for an audited sample. |
| `visual_quality` | `good`, `medium`, `poor` | Image interpretability. |
| `label_alignment` | `good`, `questionable`, `bad` | Whether label aligns with apparent change. |
| `cloud_shadow_issue` | `none`, `minor`, `severe` | Cloud, shadow, haze, smoke interference. |
| `water_issue` | `none`, `minor`, `severe` | Water or river-related interference. |
| `boundary_confidence` | `high`, `medium`, `low` | Confidence in label boundary quality. |
| `reviewer` | string | Reviewer name or anonymized reviewer ID. |
| `review_date` | date | Recommended format: YYYY-MM-DD. |
| `notes` | free text | Short issue description when needed. |

## Recommended checks after metadata edits

After any metadata or split change, rerun structure and reliability checks, then regenerate `checksums.sha256` before public release.
