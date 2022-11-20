import argparse
import subprocess
from pathlib import Path
import shutil

REPO_URL = "https://github.com/Tobi-De/fuzzy-couscous"


def cli():
    """
    A basic script that initializes a django project from my fuzzy-couscous project template.
    The purpose of this script is to remove unnecessary folders and files from the generated template.
    It is also a shortcut to avoid typing the full django-admin command with all the options.
    """
    parser = argparse.ArgumentParser(
        prog="fuzzy-couscous",
        description="Initialize a new django project using the fuzzy-couscous project templat.",
    )
    parser.add_argument("project_name")
    parser.add_argument("-b", "--branch", default="main")
    args = parser.parse_args()

    url = REPO_URL + f"/archive/{args.branch}.zip"
    project_name = args.project_name.strip().replace(" ", "_")

    # run the django-admin command
    subprocess.run(
        [
            "django-admin",
            "startproject",
            project_name,
            "--template",
            url,
            "-e=py,html,toml,md",
        ]
    )

    # since the root dir and the real project dir have the same name, rename the root to avoid conflict
    project_root_dir = Path() / project_name
    project_root_new_dir = Path() / f"_root_{project_root_dir}"
    project_root_dir.rename(str(project_root_new_dir))

    # move the real project dir to the current working directory
    project_dir = project_root_new_dir / project_name
    new_project_dir = Path() / project_name
    shutil.move(project_dir, new_project_dir)

    # delete the root dir
    shutil.rmtree(project_root_new_dir)
