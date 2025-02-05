import requests
import os
import json

GITHUB_API = "https://api.github.com"
TOKEN = os.getenv("GH_PAT")
USERNAME = os.getenv("GH_USERNAME")
ORG_NAME = os.getenv("GH_ORG_NAME")

headers = {"Authorization": f"Bearer {TOKEN}"}

def get_org_repos():
    """ 조직의 모든 레포 가져오기 (비공개 포함) """
    repos = []
    page = 1
    while True:
        url = f"{GITHUB_API}/orgs/{ORG_NAME}/repos?type=all&per_page=100&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("❌ Error fetching repositories:", response.json())
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def get_user_contributions(repo_name):
    """ 특정 레포에서 사용자의 커밋 수 가져오기 """
    url = f"{GITHUB_API}/repos/{repo_name}/commits?author={USERNAME}&per_page=100"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"⚠️ {repo_name}에서 커밋 데이터를 가져오지 못함.")
        return 0
    commits = response.json()
    return len(commits)

def main():
    repos = get_org_repos()
    total_contributions = 0

    if not repos:
        print("❌ No repositories found.")
        return

    contributions_data = {}

    for repo in repos:
        repo_name = repo["full_name"]
        contributions = get_user_contributions(repo_name)
        print(f"{repo_name}: {contributions} commits")
        total_contributions += contributions
        contributions_data[repo_name] = contributions

    # JSON 저장
    with open("contributions.json", "w") as f:
        json.dump({"total_contributions": total_contributions, "details": contributions_data}, f, indent=4)

    print(f"✅ 총 커밋 수: {total_contributions}")

if __name__ == "__main__":
    main()
