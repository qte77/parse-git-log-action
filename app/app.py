"""Entry point to the app"""

from sys import exit
from subprocess import run
from utils import get_parsed_diff


def main() -> None:
    """Main function of the app"""
    commit_1 = 'e74867104f8292ecc125559a6164bc6542228514'
    commit_2 = 'e36027808600853749d7fa332695e4078df48b92'
    
    #user = 'qte77'
    #repo = 'parse-git-log-action'
    #gh_ul = f"github.com/{user}/{repo}/compare/{commit_1}...{commit_2}"
    
    diff_run = run(["git", "diff", commit_1, commit_2], capture_output=True)
    print(diff_run)
    
    diff_output = diff_run.stdout.decode("utf-8")
    print(diff_output)

    summary = get_parsed_diff(diff_output)
    print(summary)


if __name__ == "__main__":
    exit(main())
