import os
import time
from datetime import datetime, timedelta
from random import randint

# GitHub credentials
GITHUB_USERNAME = "MuhirwaVerygood"
GITHUB_PASSWORD = "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"

# Configure git to store credentials (this will save them for future use)
os.system(f'git config --global credential.helper "store --file ~/.git-credentials"')

# Alternatively, you can include credentials directly in the remote URL
os.system(f'git remote set-url origin https://{GITHUB_USERNAME}:{GITHUB_PASSWORD}@github.com/MuhirwaVerygood/python_t_commt_gthb.git')

start_date = datetime.now() - timedelta(days=365 * 1)  # Start 1 year ago

for i in range(1000):  # Number of commits
    commit_date = start_date + timedelta(days=randint(0, 365))  # Random past date within 1 year
    commit_date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    with open("hello.txt", "a") as f:
        f.write(f"Commit {i+1} on {commit_date_str}\n")

    os.system("git add .")
    os.system(f'GIT_COMMITTER_DATE="{commit_date_str}" git commit --date="{commit_date_str}" -m "Commit {i+1}"')
    
    # Push with credentials in URL (alternative method)
    os.system(f'git push https://{GITHUB_USERNAME}:{GITHUB_PASSWORD}@github.com/MuhirwaVerygood/python_t_commt_gthb.git main')
    
    time.sleep(2)  # Avoid rate limiting

print("All commits pushed successfully!")