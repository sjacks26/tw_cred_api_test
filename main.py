import tweepy
import json

creds_file = ''
number_of_pings_per_app = 3

with open(creds_file) as f:
    creds_json = f.read()

creds_json = eval(creds_json)
creds = creds_json['apps']

for i in range(0,number_of_pings_per_app):
    for cred in creds:
        print(cred['Twitter app'])
        api_auth = tweepy.OAuthHandler(cred['consumer key'], cred['consumer secret'])
        api_auth.set_access_token(cred['access token'], cred['access token secret'])
        api = tweepy.API(api_auth)
        api.verify_credentials()
        print("Success!")
        print(api.rate_limit_status()['resources']['account']['/account/verify_credentials']['remaining'])
