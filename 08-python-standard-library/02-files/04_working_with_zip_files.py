from pathlib import Path
from zipfile import ZipFile

# # Writing in Zip file

# with ZipFile("file.zip", "w") as zip:
#     for path in Path("08-python-standard-library").rglob("*.*"):
#         zip.write(path)

# # Reading from Zip file

with ZipFile("file.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("08-python-standard-library/01-path/01_path.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")