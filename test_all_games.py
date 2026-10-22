# -*- coding: utf-8 -*-
import json
import os
import urllib.request

with open(r"apps\retrohub\games_data.js", "r", encoding="utf-8") as f:
    text = f.read()

json_str = text.split("const GAMES_CATALOG = ")[1].strip().rstrip(";")
catalog = json.loads(json_str)

print(f"Total entries in catalog: {len(catalog)}")

local_ok = 0
local_missing = []
missing_props = []

for idx, g in enumerate(catalog):
    # Check props
    for prop in ["id", "title_he", "title_en", "cat", "url", "icon"]:
        if prop not in g or not g[prop]:
            missing_props.append((idx, g.get("id"), prop))
            
    # Check local files
    if g.get("is_offline"):
        path = os.path.join(r"apps\retrohub", g["url"].replace("/", "\\"))
        if os.path.exists(path):
            local_ok += 1
        else:
            local_missing.append((g["id"], path))

print(f"Local offline engines tested: {local_ok}/{len([g for g in catalog if g.get('is_offline')])} valid.")
if local_missing:
    print(f"Missing local files: {local_missing}")
if missing_props:
    print(f"Missing props: {missing_props[:10]}")
