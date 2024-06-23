'''Entry point to the app'''

from os import getenv
from sys import exit
from pathlib import Path
from subprocess import run
from utils import get_parsed_diff, get_git_diff


def main() -> None:
    '''Main function of the app'''
    # TODO assert env OUT_FILE can be converted to POSIX PAth
    OUT_FILE = Path(getenv("OUT_FILE", 'data/dummy-data.md'))
    CMD_HIGHLIGHT = str(getenv("CMD_HIGHLIGHT", 'sh'))
    # TODO check getenv for bool
    DRY_RUN  = bool(getenv("CMD_HIGHLIGHT", False))
    
    commit_1 = 'e74867104f8292ecc125559a6164bc6542228514'
    commit_2 = 'e36027808600853749d7fa332695e4078df48b92'
    #user = 'qte77'
    #repo = 'parse-git-log-action'
    #gh_ul = f"github.com/{user}/{repo}/compare/{commit_1}...{commit_2}"

    summary = get_parsed_diff(get_git_diff(commit_1, commit_2))

    if DRY_RUN:
        print(summary)
    else:
        if not OUT_FILE.parent.exists():
          # folder needs to exist before open() context
          OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(OUT_FILE, 'a+', newline=None, encoding='UTF8') as f:
            f.write(summary)


if __name__ == "__main__":
    exit(main())
