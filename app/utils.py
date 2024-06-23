from datetime import datetime, timezone
from subprocess import run


def _parseGitDiff(diffs: list) -> list:
	'''TODO'''
	summary = []
	hunk_literal = "@@"
	hunk_line_suffix = "Lines changed (start at, count): "
	hunk_line_sep = " "
	start_of_line = {
		"similarity": "similar% ",
		"new file": "created  ",
		"deleted": "deleted  ",
		"rename": "rename   ",
		"diff --git": "difference between",
		"---": "renamed/deleted from",
		"+++": "renamed/deleted to  ",
		hunk_literal: ["source ", "new file "],
		"-": "removed  ",
		"+": "added    "
	}
	# TODO sort descending, get unique
	sol_key_len = len(start_of_line)
	for line in diffs:
    for sol in sol_key_len:
      line_start = str(line[:sol])
      if line_start.startswith(hunk_literal):
        hunk = line.split(hunk_literal).strip()
        range = hunk[1].split()
        summary.append(
          hunk_line_suffix + start_of_line[hunk_literal][0] + \
          range[0] + hunk_line_sep + \
          start_of_line[hunk_literal][1] + range[1]
        )
      else:
        if "+" in line_start:
          # TODO escape char for regexp
          # rex_ls = line_start.replace('+', '\+')
          # TODO replace regexp rex_ls in line with " "
          # summary.append(start_of_line[line_start] + rex_ls_replace_in_line)
	return summary


def get_git_diff(commit_1: str, commit_2: str) -> str:
	'''TODO'''
	diff_run = run(["git", "diff", commit_1, commit_2], capture_output=True)
	return diff_run.stdout.decode("utf-8")


def parse_git_diff(diff_output: list) -> str:
	'''TODO'''
	summary = []
	
	# commits_last = git log --format="%H" -n commits_num
	# commits_last_len = len(commits_last)
	# commits_num = 20
	# date_utc = datetime.now(timezone.utc)
	# save_path = "."

	print('parse_git_diff')

	summary.append(f"\n{datetime.now(timezone.utc)}")
	for line in diff_output:
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
	
