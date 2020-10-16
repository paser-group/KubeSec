# coding: utf-8

"""
Courtesy Jonathon Alexander Gibson
"""

import git
import requests
from git import GitCommandError

# insert  Personal Authentication Token (PAT)
AUTH = ("username", "PAT")

def main():
    all_urls = []  # list to store all URLs from the multiple JSON responses
    url_count = 0

    # Collect first 1000 repositories
    for p in range(1, 11):
        print("Page:", p)
        p_req = requests.get("https://api.github.com/search/repositories?q=kubernetes,microservice" + "?&page=" + str(p) + "&per_page=100" + "&sort=stars&order=desc", auth=AUTH)
        p_res = p_req.json()
        try:
            items = p_res["items"]
            # print(items)
        except Exception as e:
            print(e)
        urls = [item["html_url"] for item in items]  # make temporary list of URLs from the current JSON response on page <p> for year range <y>
        url_count += len(urls)
        all_urls.extend(urls)
        print(len(all_urls))
    # remove repetition from multiple iterations
    urls_set = set(all_urls)

    clone_count = 0
    cloned_repos_dir = "/Users/shamim/Downloads/k8s_data"

    for repo in urls_set:
        clone_count += 1
        repo = repo.lstrip("https://")
        repo_remote_path = "git://" + repo + ".git"
        print(clone_count, "––– Cloning repository –––", repo_remote_path)
        try:
            git.Git(cloned_repos_dir).clone(repo_remote_path)
        except GitCommandError as error:
            print(error.stderr)
if __name__ == "__main__":
    main()
