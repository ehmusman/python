from pathlib import Path

# module for human read able time
from time import ctime

path = Path("08-python-standard-library/01-path/01_path.py")

print(path.stat())
print(ctime(path.stat().st_ctime))

print(path.read_bytes())
print(path.read_text())

# Copying a file
# this is not a good way to copy.
# we have shutil module to handle all the high level tasks
source = Path("08-python-standard-library/01-path/01_path.py")
target = Path("08-python-standard-library/01-path/new_dir_new") / "copy.py"

# target.write_text(source.read_text())

import shutil

shutil.copy(source, target)