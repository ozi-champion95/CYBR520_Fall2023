"""
Run this code after done install all.
"""
import sys
import os
import platform
import subprocess
import pandas


def main():
    print("data")


def check_python():
    print("Python version:")
    print(sys.version)
    print("Python executable path:")
    print(sys.executable)


def check_system_info():
    print("\nSystem information:")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")


def check_git():
    try:
        subprocess.check_output(['git', '--version'])
        print("\nGit is installed.")
    except FileNotFoundError:
        print("\nGit is not installed.")


def check_pycharm():
    try:
        subprocess.check_output(['pycharm', '--version'])
        print("\nPyCharm is installed.")
    except FileNotFoundError:
        print("\nPyCharm is not installed.")


if __name__ == "__main__":
    print("Checking Python installation:")
    check_python()

    print("\nChecking system information:")
    check_system_info()

    print("\nChecking Git installation:")
    check_git()

    print("\nChecking PyCharm installation:")
    check_pycharm()

if __name__ == "__main__":
    main()
