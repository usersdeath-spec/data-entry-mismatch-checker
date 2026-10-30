# Data Entry Mismatch Checker

BPO teams often have two people enter the same records independently, then compare the two versions
(double-entry verification). This script automates that comparison.

## What it does
- Compares two CSV files record by record, field by field
- Flags every mismatch (for example a typo in a name, swapped digits in a phone number or amount)
- Lists records present in one file but missing in the other
- Reports field-level accuracy

## How to run
```
pip install pandas
python check.py entry_a.csv entry_b.csv
```
Outputs: `mismatches.csv` and `summary.txt`.

## Sample result
Catches `Varma` vs `Verma`, `1800` vs `1080` and `9123412345` vs `9123412354`, plus records missing from either file.
See `summary.txt`.

*Sample data is fictional.*
