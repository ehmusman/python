import subprocess

try:
    result = subprocess.run(
        ["false"]
        # ["python3", "08-python-standard-library/child.py"]
        , capture_output=True, text=True, check=True)

    print("args", result.args)
    print("returncode", result.returncode)
    print("stderr", result.stderr) # any non zero is error
    print("stdout", result.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)