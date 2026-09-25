import os
import sys
import subprocess

def install_dependencies():
    requirements = ["pygame"]
    for package in requirements:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def create_structure():
    directories = [
        "src",
        "tools/app",
        "assets/images",
        "assets/sounds"
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

if __name__ == "__main__":
    create_structure()
    install_dependencies()
