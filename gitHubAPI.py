#Stevens Institute of Technology - Fall 2022
# SSW 567 - Software Testing, Quality Assurance and Maintenance
# Nathalie Souza
# Homework Assignment #4a

# I pledge that I have abided by the Stevens honor system.


import requests
import json


def gitHubAPI(user_ID):
    #This takes in the users repo information 
    repos = "https://api.github.com/users/" + user_ID + "/repos"
    results = requests.get(repos)

    repo_list = results.json()
    
    # Adds the repos into a dictionary
    repo_dict = {}

    for repo in repo_list:
        # print(repo["name"])
        commitsAPI = "https://api.github.com/repos/" + user_ID +"/" + repo["name"] +"/commits"
        user_commits = requests.get(commitsAPI)
        num = json.loads(user_commits.content.decode('utf-8'))

        print(" Repo: " + repo["name"] + " Number of Commits: " + str(len(num)))

        repo_dict[(str(repo["name"]))] = len(num)
    # print(repo_dict)
    return repo_dict



if __name__ == "__main__":
    gitHubAPI("nathsouza")