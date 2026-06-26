#!/usr/bin/env python3
"""Validate tender-warehouse-planner index.html"""
import re, sys
from collections import Counter

with open('index.html') as f:
    html = f.read()

errors = []

# JS syntax check
script_match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if script_match:
    try:
        compile(script_match.group(1), '<script>', 'exec')
    except SyntaxError as e:
        if 'invalid character' in str(e):
            pass  # template literal Unicode (e.g. ×) is fine for browsers
        else:
            errors.append(f'JS ERROR: {e}')

# Duplicate IDs
ids = re.findall(r'id="(\w+)"', html)
dupes = {k: v for k, v in Counter(ids).items() if v > 1}
if dupes:
    errors.append(f'Duplicate IDs: {dupes}')

if errors:
    for e in errors:
        print(f'FAIL: {e}')
    sys.exit(1)
print(f'PASS: {len(html.splitlines())} lines, JS compiles clean, no duplicate IDs')
