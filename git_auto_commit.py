import os
import time

for i in range(10000):  # Change 10 to the number of commits you want
    with open("hello.txt", "a") as f:
        f.write(f"Commit {i+1}\n")
    os.system("git add .")
    os.system(f'git commit -m "Automated commit {i+1}"')
    os.system("git push origin main")  # Change 'main' if using a different branch
    time.sleep(2)  # Delay to avoid rate limiting
