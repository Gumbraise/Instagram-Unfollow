from InstagramAPI import InstagramAPI
import time
import requests
import json

username = input("Put your IG Username then press ENTER: ")
password = input("Put your IG Password then press ENTER: ")
api = InstagramAPI(username, password)
api.login()

following = api.getTotalSelfFollowings()
for k, v in enumerate(following):
    user = v['pk']
    username = v["username"]

    api.unfollow(user)
    print(username + " is now unfollowed")
