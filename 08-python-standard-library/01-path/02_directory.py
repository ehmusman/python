from pathlib import Path


path = Path("08-python-standard-library/01-path/new_dir")

print(path.exists())
path.mkdir(parents=True, exist_ok= True)

path.rename("08-python-standard-library/01-path/new_dir_new")

# path.rmdir()

path = Path("08-python-standard-library")

dir_contents_generator = path.iterdir()
# it's returning a generator object. if we have millions of file in a directory, it's helpfull. if we have a few files, we can convert it to list.
for item in dir_contents_generator:
    print(item)

all_files = [p for p in path.iterdir()]
print(all_files)

all_dir = [p for p in path.iterdir() if p.is_dir()]
print(all_dir)

# paths are of two types, windows path and PosixPath
# PosixPath is used in cased of unix OS

# path.iterdir() has two limitations. it can't search by pattern. it can't search recursively

# we can use glob for this
all_files = [p for p in path.iterdir()]
path.glob("*.*") # returning all files
path.glob("*.py") # returning all py files

path = Path("08-python-standard-library/01-path")

all_py_files = [p for p in path.glob("*.py")]
print(all_py_files)

# recursive glob
# recursive means searching in sub directories
path = Path("08-python-standard-library")

all_py_files = [p for p in path.rglob("**/*.py")]
print(all_py_files)