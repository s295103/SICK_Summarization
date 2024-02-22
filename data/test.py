import json

data = {'dialogue': [],'summary':[],'id':[]}
with open("tweetsumm_test.json", 'r') as f:
    json_dict = json.load(f)
    data["id"] = list(json_dict.keys())
    data['dialogue'] = [v["turns"] for v in json_dict.values()]
    data['summary'] = [v["summaries"] for v in json_dict.values()]
    
pass