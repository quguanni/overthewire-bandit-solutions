#!/usr/bin/env python3
# summarize_results.py
import csv
from collections import defaultdict, Counter
import json

IN="results.csv"
def load_rows(fname):
    rows=[]
    with open(fname, newline='') as f:
        r=csv.DictReader(f)
        for row in r:
            # normalize
            row['attack_success']=int(row.get('attack_success') or 0)
            row['time_ms']=int(row.get('time_ms') or 0)
            rows.append(row)
    return rows

rows = load_rows(IN)

# 1) Per-attack, per-defense stats
stats = {}
by_defense = defaultdict(lambda: {"trials":0,"successes":0})
by_attack_def = defaultdict(lambda: {"trials":0,"successes":0})
examples_success = defaultdict(list)

for r in rows:
    k=(r['attack_id'], r['defense'])
    by_attack_def[k]['trials'] += 1
    by_defense[r['defense']]['trials'] += 1
    if r['attack_success']:
        by_attack_def[k]['successes'] += 1
        by_defense[r['defense']]['successes'] += 1
        # collect up to 3 example transcripts per (attack,defense)
        if len(examples_success[k]) < 3:
            examples_success[k].append((r['trial_id'], r['tool_called'], r['tool_arg'], r['note']))

# Print table per-attack per-defense
print("Per-attack / per-defense success rates\nattack_id,defense,success_rate,successes,trials")
for (attack_id, defense), v in sorted(by_attack_def.items()):
    rate = v['successes']/v['trials'] if v['trials'] else 0
    print(f"{attack_id},{defense},{rate:.2f},{v['successes']},{v['trials']}")

# 2) Overall defense rates & deltas vs baseline
baseline = by_defense.get('none', {"trials":0,"successes":0})
base_rate = baseline['successes']/baseline['trials'] if baseline['trials'] else None
print("\nOverall defense rates and delta vs baseline (baseline='none')\ndefense,success_rate,successes,trials,delta_vs_baseline")
for d, v in by_defense.items():
    rate = v['successes']/v['trials'] if v['trials'] else 0
    if base_rate is None:
        delta = "N/A"
    else:
        delta = f"{(base_rate-rate):+.2f}"
    print(f"{d},{rate:.2f},{v['successes']},{v['trials']},{delta}")

# 3) Time stats (mean per defense)
from statistics import mean
time_by_def = defaultdict(list)
for r in rows:
    time_by_def[r['defense']].append(r['time_ms'])
print("\nAverage time_ms per defense (note: 0 means not instrumented)")
for d, lst in time_by_def.items():
    print(f"{d}: mean={mean(lst):.1f}ms n={len(lst)}")

# 4) Output example successful transcripts for manual triage
print("\nExample successful transcripts (up to 3 each) — (attack_id, defense, trial_id, tool_called, tool_arg, note)")
for (attack_id, defense), samples in examples_success.items():
    for s in samples:
        print(f"{attack_id},{defense},{s[0]},{s[1]},{s[2]},note={s[3]}")

# 5) Write summary CSV per defense
OUT="summary_by_defense.csv"
with open(OUT,"w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["defense","success_rate","successes","trials"])
    for d,v in by_defense.items():
        rate = v['successes']/v['trials'] if v['trials'] else 0
        writer.writerow([d, f"{rate:.4f}", v['successes'], v['trials']])
print(f"\nWrote summary_by_defense.csv")
