import json

string_as_json_format = '{"companyName": "Lowes of Lawrenceburg,IN","companyId": 24345,"address": "970 W. Eads Parkway, Lawrenceburg, IN 47025-1168","city": "Lawrenceburg","state": "IN","zip": "47025-1168","distance": 5.46085253241915,"adPatchId": 83}'
obj = json.loads(string_as_json_format)
print(obj['companyName'])

