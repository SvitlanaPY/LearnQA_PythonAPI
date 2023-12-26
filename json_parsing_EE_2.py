import json

string_as_json_format = '''[
    {
        "companyId": 24345,
        "companyName": "Lowe's of Lawrenceburg,IN",
        "address": "970 W. Eads Parkway, Lawrenceburg, IN 47025-1168",
        "city": "Lawrenceburg",
        "state": "IN",
        "zip": "47025-1168",
        "distance": 5.46085253241915,
        "adPatchId": 83
    },
    {
        "companyId": 24203,
        "companyName": "Lowe's of Cincinnati,OH",
        "address": "6150 Harrison Road, Cincinnati, OH 45247",
        "city": "Cincinnati",
        "state": "OH",
        "zip": "45247",
        "distance": 13.1061422475141,
        "adPatchId": 83
    },
    {
        "companyId": 23251,
        "companyName": "Lowe's of Cincinnati,OH",
        "address": "10235 Colerain Ave., Cincinnati, OH 45251",
        "city": "Cincinnati",
        "state": "OH",
        "zip": "45251",
        "distance": 16.758855692497,
        "adPatchId": 83
    },
    {
        "companyId": 23269,
        "companyName": "Lowe's of Florence,KY",
        "address": "4800 Houston Road, Florence, KY 41042",
        "city": "Florence",
        "state": "KY",
        "zip": "41042",
        "distance": 17.3156686452035,
        "adPatchId": 83
    },
    {
        "companyId": 23036,
        "companyName": "Lowe's of Hamilton,OH",
        "address": "1495 Main St., Hamilton, OH 45013",
        "city": "Hamilton",
        "state": "OH",
        "zip": "45013",
        "distance": 23.858007180406,
        "adPatchId": 83
    }
]'''
obj = json.loads(string_as_json_format)
print(obj[0]['companyName'])
