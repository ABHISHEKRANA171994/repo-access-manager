import os
import requests

# GitHub Personal Access Token (PAT) from environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_ORG = "your_github_organization"  # Replace with your GitHub organization name

# Function to add team access to a repository
def add_team_access(team_name, repo_name, permission):
    url = f"https://api.github.com/orgs/{GITHUB_ORG}/teams/{team_name}/repos/{GITHUB_ORG}/{repo_name}"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    payload = {
        "permission": permission  # Can be 'push', 'pull', or 'admin'
    }

    response = requests.put(url, headers=headers, json=payload)

    if response.status_code == 204:
        print(f"Team '{team_name}' granted '{permission}' access to '{repo_name}' repository.")
    else:
        print(f"Failed to grant access for '{repo_name}': {response.status_code} - {response.text}")

# Main function to handle input parameters and process each repository
def main():
    import sys
    team_name = sys.argv[1]
    repo_names = sys.argv[2]
    permission = sys.argv[3]

    # Split comma-separated repo names
    repo_list = [repo.strip() for repo in repo_names.split(",")]

    for repo in repo_list:
        add_team_access(team_name, repo, permission)

if __name__ == "__main__":
    main()
