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
    user = item["username"]

    url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+user+"&rank_token=0.3953592318270893&count=1"
    response = requests.get(url)
    respJSON = response.json()
    user_id = str( respJSON['users'][0].get("user").get("pk") )

    api.unfollow(user_id)
    print(user + " is now unfollowed")