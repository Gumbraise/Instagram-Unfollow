from InstagramAPI import InstagramAPI
import time
import requests
import json

username = input("Put your IG Username then press ENTER: ")
password = input("Put your IG Password then press ENTER: ")
api = InstagramAPI(username, password)
api.login()

following = api.getSelfUsersFollowing()

for item in following["users"]:
    user = item["pk"]
    username = item["username"]

    api.unfollow(user)
    print(username + " is now unfollowed")