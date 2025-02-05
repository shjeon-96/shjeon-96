import requests
import os
import json

GITHUB_API = "https://api.github.com"
TOKEN = os.getenv("GH_PAT")
USERNAME = os.getenv("GH_USERNAME")
ORG_NAME = os.getenv("GH_ORG_NAME")

headers = {"Authorization": f"token {TOKEN}"}

def get_org_repos():
    """ 조직의 모든 레포 가져오기 (비공개 포함) """
    repos = []
    page = 1
    while True:
        url = f"{GITHUB_API}/orgs/{ORG_NAME}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Error fetching repositories:", response.json())
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def get_user_contributions(repo_name):
    """ 특정 레포에서 사용자의 커밋 수 가져오기 """
    url = f"{GITHUB_API}/repos/{repo_name}/contributors"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    contributors = response.json()
    for contributor in contributors:
        if contributor["login"] == USERNAME:
            return contributor["contributions"]
    return 0

def main():
    repos = get_org_repos()
    total_contributions = 0

    if not repos:
        print("No repositories found.")
        return

    for repo in repos:
        repo_name = repo["full_name"]
        contributions = get_user_contributions(repo_name)
        print(f"{repo_name}: {contributions} commits")
        total_contributions += contributions

    with open("contributions.json", "w") as f:
        json.dump({"total_contributions": total_contributions}, f, indent=4)

    print(f"✅ 총 커밋 수: {total_contributions}")

if __name__ == "__main__":
    main()
