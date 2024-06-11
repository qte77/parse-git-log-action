"""parse commits"""
from datetime import datetime, timezone 


def _parseGitDiff(diffs: list) -> parsedDiffs: list:
	""""""
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
          rex_ls = line_start.replace('+', '\+')
          # TODO replace regexp rex_ls in line with " "
          # summary.append(start_of_line[line_start] + rex_ls_replace_in_line)
  return summary


commits_last = git log --format="%H" -n commits_num
commits_last_len = len(commits_last)


commits_num = 20
date_utc = datetime.now(timezone.utc)
save_path = ."

