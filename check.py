"""Compare two independent data entries of the same records and flag every mismatch."""
import sys
import pandas as pd

def main(file_a="entry_a.csv", file_b="entry_b.csv", key="record_id"):
    a = pd.read_csv(file_a, dtype=str).set_index(key)
    b = pd.read_csv(file_b, dtype=str).set_index(key)

    only_a = sorted(set(a.index) - set(b.index))
    only_b = sorted(set(b.index) - set(a.index))
    common = sorted(set(a.index) & set(b.index))

    rows = []
    for rid in common:
        for col in a.columns:
            va, vb = str(a.loc[rid, col]).strip(), str(b.loc[rid, col]).strip()
            if va != vb:
                rows.append({key: rid, "field": col, "entry_a": va, "entry_b": vb})
    mism = pd.DataFrame(rows, columns=[key, "field", "entry_a", "entry_b"])
    mism.to_csv("mismatches.csv", index=False)

    total_fields = len(common) * len(a.columns)
    acc = 100 * (1 - len(mism) / total_fields) if total_fields else 0
    with open("summary.txt", "w") as f:
        f.write("DOUBLE-ENTRY CHECK SUMMARY\n==========================\n")
        f.write(f"Records compared        : {len(common)}\n")
        f.write(f"Fields compared         : {total_fields}\n")
        f.write(f"Mismatched fields       : {len(mism)}\n")
        f.write(f"Field-level accuracy    : {acc:.1f}%\n")
        f.write(f"Missing in entry B      : {', '.join(only_a) or 'none'}\n")
        f.write(f"Missing in entry A      : {', '.join(only_b) or 'none'}\n")
    print(open("summary.txt").read()); print(mism.to_string(index=False))

if __name__ == "__main__":
    main(*sys.argv[1:])
