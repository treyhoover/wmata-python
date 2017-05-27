# python 3.6
api_key = "e1eee2b5677f408da40af8480a5fd5a8"

import requests
# import json

base_url = 'https://api.wmata.com'

headers = {
    'api_key': api_key,
}

params = {}

try:
    res = requests.get(
        base_url + "/Incidents.svc/json/Incidents",
        headers=headers,
        params=params
    )

    data = res.json()
    incidents = data.get('Incidents')

    lines_affected = set(
        ' '.join([i.get('LinesAffected') for i in incidents])
           .replace(';', '')
           .split(' ')
    )

    print("There are %s reported incidents.\n" % len(incidents))

    if len(lines_affected) > 0:
        print("{} lines are affected:".format(len(lines_affected)))
        for line in lines_affected:
            print("  {}".format(line))

    # print(json.dumps(data, indent=4))
except Exception as e:
    print("error: ", e)