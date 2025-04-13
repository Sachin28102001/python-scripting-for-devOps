#Python program to fetch all the datas from a Github Repo of all the users who made a pull reqs.

import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_info = response.json()


for i in range(len(complete_info)):
    print(complete_info[i]["user"]["login"])
