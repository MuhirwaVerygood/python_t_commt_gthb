import os
import time
from datetime import datetime, timedelta
from random import randint

# Configuration
USERNAME = "MuhirwaVerygood"
TOKEN = "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"  # Your GitHub Personal Access Token
REPO_NAME = "python_t_commt_gthb"
EMAIL = "verygoodmuhirwa22@gmail.com"  # Your GitHub email

def setup_https_authentication():
    """Configure HTTPS authentication with credential store"""
    # Store credentials in plaintext (only for this repo)
    os.system('git config --global credential.helper "store --file ~/.git-credentials"')
    
    # Write credentials to file
    with open(os.path.expanduser("~/.git-credentials"), "w") as f:
        f.write(f"https://{USERNAME}:{TOKEN}@github.com\n")
    
    # Set remote URL
    os.system(f'git remote set-url origin https://github.com/{USERNAME}/{REPO_NAME}.git')
    
    # Configure user info
    os.system(f'git config --global user.name "{USERNAME}"')
    os.system(f'git config --global user.email "{EMAIL}"')

def make_commit(commit_num):
    """Create a commit with random date"""
    start_date = datetime.now() - timedelta(days=365)
    commit_date = start_date + timedelta(days=randint(0, 365))
    commit_date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    # Create or modify a file
    with open("auto_commits.txt", "a") as f:
        f.write(f"Commit {commit_num} on {commit_date_str}\n")

    # Stage and commit changes
    os.system("git add .")
    os.system(f'GIT_COMMITTER_DATE="{commit_date_str}" git commit --date="{commit_date_str}" -m "Auto commit {commit_num}"')

def push_changes():
    """Push changes to remote repository"""
    return os.system("git push origin main") == 0

def main():
    # Setup authentication (only needed once)
    setup_https_authentication()
    
    # Create initial file if it doesn't exist
    if not os.path.exists("auto_commits.txt"):
        with open("auto_commits.txt", "w") as f:
            f.write("Initial commit file\n")
        os.system("git add auto_commits.txt")
        os.system('git commit -m "Initial commit"')
        push_changes()
    
    # Commit loop
    for i in range(1, 1001):  # 1000 commits
        make_commit(i)
        
        # Push changes with retry logic
        if not push_changes():
            print(f"Push failed for commit {i}, retrying after delay...")
            time.sleep(30)
            push_changes()
        
        # Random delay to appear natural and avoid rate limiting (5-60 seconds)
        delay = randint(5, 60)
        print(f"Commit {i} pushed. Waiting {delay} seconds...")
        time.sleep(delay)
    
    print("All commits pushed successfully!")

if __name__ == "__main__":
    main()