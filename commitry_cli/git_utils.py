import subprocess

def get_staged_diff():
    """Return the staged diff as a string."""
    # Alternatively, you can use GitPython
    result = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True)
    return result.stdout
