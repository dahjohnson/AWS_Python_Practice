import http.client
import requests, json

conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
    'x-rapidapi-key': "****"
    }

conn.request("GET", "/standings?league=standard&season=2022", headers=headers)

res = conn.getresponse()
res = res.read()
jsonres = json.loads(res.decode('utf-8'))
jsonres_format = json.dumps(jsonres, indent=2)

print(jsonres_format)