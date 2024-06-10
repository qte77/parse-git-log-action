#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Entry point to the app"""

from sys import exit
from subprocess import run


def parse_git_diff(diff_output: str):
    '''TODO'''
    lines = diff_output.split('\n')
    summary = []

    print('parse_git_diff')
    
    for line in lines:
        if line.startswith('+'):
            summary.append(f"Added line: {line[1:]}")
        elif line.startswith('-'):
            summary.append(f"Removed line: {line[1:]}")
        elif line.startswith('@@'):
            hunk_info = line.split('@@')
            original_range = hunk_info[1].strip().split(' ')[1]
            modified_range = hunk_info[2].strip()
            summary.append(f"Changes in lines {original_range} of the original file and {modified_range} of the modified file")

    return '\n'.join(summary)


def main() -> None:
    """Main function of the app"""
    commit_1 = 'e74867104f8292ecc125559a6164bc6542228514'
    commit_2 = 'e36027808600853749d7fa332695e4078df48b92'
    
    #user = 'qte77'
    #repo = 'parse-git-log-action'
    #gh_ul = f"github.com/{user}/{repo}/compare/{commit_1}...{commit_2}"
    
    diff_run = run(["git", "diff", "$commit_1", "$commit_2"], capture_output=True)
    print(diff_run)
    
    diff_output = diff_run.stdout.decode("utf-8")
    print(diff_output)
    
    summary = parse_git_diff(diff_output)
    print(summary)


if __name__ == "__main__":
    exit(main())
