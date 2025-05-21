import os
import subprocess
from datetime import datetime

def git_commit(commit_message="Automated commit", add_all=True):
    """
    Automates the process of adding changes, committing, and pushing to a Git repository.

    Args:
        commit_message (str, optional): The message for the commit. Defaults to "Automated commit".
        add_all (bool, optional): Whether to add all changes. If false, only explicitly added files are committed.
    """
    try:
        if add_all:
            subprocess.run(["git", "add", "-u"], check=True, capture_output=True)
            subprocess.run(["git", "commit", "-m", commit_message], check=True, capture_output=True)
        print("Git commit and push successful.")

    except subprocess.CalledProcessError as e:
        print(f"Error during Git operation: {e}")
        print(e.stderr.decode())

if __name__ == "__main__":
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    git_commit(f"Automated commit on {now}")
