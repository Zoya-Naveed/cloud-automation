import os
import subprocess

TERRAFORM_DIR = "../terraform"

def run_terraform(command):
    os.chdir(TERRAFORM_DIR)
    print(f"Running: terraform {command}")
    result = subprocess.run(f"terraform {command}", shell=True)
    if result.returncode != 0:
        print(f"Error running terraform {command}")
    else:
        print(f"Completed: terraform {command}")

def init():
    run_terraform("init")

def plan():
    run_terraform("plan")

def apply():
    print("WARNING: Offline-safe demo. Will only run plan.")
    plan()

def destroy():
    print("WARNING: Offline-safe demo. Will only run plan.")
    plan()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Manage AWS infrastructure with Terraform (offline-safe)")
    parser.add_argument("action", choices=["init", "plan", "apply", "destroy"], help="Action to perform")
    args = parser.parse_args()

    if args.action == "init":
        init()
    elif args.action == "plan":
        plan()
    elif args.action == "apply":
        apply()
    elif args.action == "destroy":
        destroy()
