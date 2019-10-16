import requests
from requests_oauthlib import OAuth1Session
import json
import os

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
url_favo = "https://api.twitter.com/1.1/favorites/create.json"

def file_read():
    dicts_from_file = []
    f = open(".oauth.txt", "r")
    for line in f:
        dicts_from_file.append(eval(line))
    return dicts_from_file

def OAuth(Consumerkey, Consumersecret, AccessToken, AccessSecret):
    return OAuth1Session(Consumerkey, Consumersecret, AccessToken, AccessSecret)

if __name__ == '__main__':
    data = file_read()
    auth = OAuth(data[0]['api_key'], data[0]['api_select'], data[0]['access_key'], data[0]['access_secret'])
    params_user = {"screen_name" : "", "count" : "1"}
    req = auth.get(url, params=params_user)
    if req.status_code == 200:
        print("success\n")
        tweet = json.loads(req.text)
        for line in tweet:
            print(line['text'])
            req_favo = auth.post(url_favo, {"id": line['id']})
            print(req_favo)
    else:
        print("error")
