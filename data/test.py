import json
import re
dir = "./tweetsumm_test.json"
with open(dir, 'r') as f:
    json_dict = json.load(f)
    id = list(json_dict.keys())
    dialogue = [v["turns"] for v in json_dict.values()]
    summary = [v["summaries"] for v in json_dict.values()]

pass