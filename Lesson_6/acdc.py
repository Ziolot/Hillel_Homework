import json
with open('acdc.json', 'r') as f:
    data = json.load(f)
count = sum(map(lambda x: int(x['duration']), data))
print(count)