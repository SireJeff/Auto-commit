import requests
import schedule
import time
import os
from datetime import datetime
import dotenv

# # GitHub credentials
# USERNAME = "your_username"
# TOKEN = "your_personal_access_token"  # Generate a token with repo access from https://github.com/settings/tokens

# # Repository information
# REPO_OWNER = "your_repo_owner"
# REPO_NAME = "your_repo_name"
# FILE_PATH = "path/to/your/file.txt"
USERNAME="SireJeff"
TOKEN="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"
REPO_OWNER="SireJeff"
REPO_NAME="web_api_sales"
FILE_PATH="./test.txt"


# # GitHub credentials
# USERNAME = os.getenv("GITHUB_USERNAME")
# TOKEN = os.getenv("GITHUB_TOKEN")

# # Repository information
# REPO_OWNER = os.getenv("REPO_OWNER")
# REPO_NAME = os.getenv("REPO_NAME")
# FILE_PATH = os.getenv("FILE_PATH")

def create_dummy_commit():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"

    # Get the current content of the file
    response = requests.get(url, headers={"Authorization": f"token {TOKEN}"})
    response.raise_for_status()
    current_content = response.json()["content"]

    # Append a character to the file content
    new_content =  "X"
    encoded_content = new_content.encode("utf-8").hex()

    # Commit the changes
    commit_message = f"Dummy commit - {datetime.now()}"
    data = {
        "message": commit_message,
        "content": encoded_content,
        "sha": response.json()["sha"],
    }
    response = requests.put(url, json=data, headers={"Authorization": f"token {TOKEN}"})
    response.raise_for_status()

    print(f"Dummy commit successful - {datetime.now()}")
create_dummy_commit()
# Schedule the job every 12 hours
schedule.every(12).hours.do(create_dummy_commit)

while True:
    schedule.run_pending()
    time.sleep(1)
