import json

data = [json.loads(scp) for scp in open('PythonCode/SCP-Database/scps.json', 'r')]

for daa in data: print(daa)