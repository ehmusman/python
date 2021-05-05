from pathlib import Path


# # absolute path
# Path("/usr/local/bin")
# # current folder path
# Path()

# # Combining two paths
# # We can combine path with string also
# Path() / Path("ecommerace") / "__init__.py"
# # home path
# Path.home()

path = Path("08-python-standard-library/01-path/file.py")
isExists = path.exists()
print(isExists)
print(path.home())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem) # return file name with out extension
print(path.suffix) # return extension
print(path.parent)

path =path.with_name("file.txt")
print(path)
print(path.absolute())

path =path.with_suffix(".txt")
print(path)
print(path.absolute())