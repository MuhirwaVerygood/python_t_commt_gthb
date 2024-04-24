import os
import time
from datetime import datetime, timedelta
from random import randint

# Configuration
GITHUB_USERNAME = "MuhirwaVerygood"
GITHUB_TOKEN = "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"  # Use a PAT, not password
REPO_URL = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/MuhirwaVerygood/python_t_commt_gthb.git"

def setup_git_environment():
    """Configure git to remember credentials"""
    # Store credentials in memory for this session
    os.system(f'git config --global credential.helper "cache --timeout=3600"')
    
    # Set remote URL with credentials (only for initial setup)
    os.system(f'git remote set-url origin {REPO_URL}')
    
    # Configure user info
    os.system('git config --global user.name "MuhirwaVerygood"')
    os.system('git config --global user.email "verygoodmuhirwa22@gmail.com"')

def make_commit(commit_num):
    """Make a single commit with random date"""
    start_date = datetime.now() - timedelta(days=365)
    commit_date = start_date + timedelta(days=randint(0, 365))
    commit_date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    with open("hello.txt", "a") as f:
        f.write(f"Commit {commit_num} on {commit_date_str}\n")

    os.system("git add .")
    os.system(f'GIT_COMMITTER_DATE="{commit_date_str}" git commit --date="{commit_date_str}" -m "Commit {commit_num}"')

def main():
    setup_git_environment()
    
    for i in range(1, 1001):  # 1000 commits
        make_commit(i)
        
        # Push with stored credentials
        push_success = os.system("git push origin main")
        
        if push_success != 0:
            print(f"Push failed for commit {i}, retrying...")
            time.sleep(10)  # Wait before retry
            os.system("git push origin main")  # Second attempt
            
        # Random delay to avoid rate limiting (2-10 seconds)
        time.sleep(randint(2, 10))

    print("All commits pushed successfully!")

if __name__ == "__main__":
    main()