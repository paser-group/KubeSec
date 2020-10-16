# coding: utf-8

"""
 --  Courtesy Jonathon Alexander Gibson
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
    for page in range(1, 11):
        #request with git AUTH to get response from github with 100 repository/page
        page_request = requests.get("https://api.github.com/search/repositories?q=kubernetes,microservice" + "?&page=" + str(page) + "&per_page=100" + "&sort=stars&order=desc", auth=AUTH)
        #Convert the response to JSON format
        page_result = page_request.json()
        try:
            # choose "items" attribute to get all the repository informations
            items = page_result["items"]
            # print(items)
        except Exception as e:
            print(e)
        # pick html_url as url for each repository
        urls = [item["html_url"] for item in items]
        url_count += len(urls)
        all_urls.extend(urls)
        print(len(all_urls))
    # remove repetition from multiple iterations
    urls_set = set(all_urls)

    clone_count = 0
    #update directory with your own directory
    cloned_repos_dir = ""

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
