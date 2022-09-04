import requests, json
import json

f = open('test.json', 'r')
json_dict = json.load(f)
ID = json_dict["ID"]


WEB_HOOK_URL = "https://hooks.slack.com/services/"
content = {'text': "{}は手が止まっています".format(ID)}
requests.post(WEB_HOOK_URL, data=json.dumps(content))
