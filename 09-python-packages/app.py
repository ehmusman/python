# Python library is not enough for real time apps
# we can navigate to pypi for checking other usefull packages


# ------------------------- Pip ---------------------------------
# pip3 list => to show all the downloaded packages.
# pip3 install requests
# pip3 install requests==2.24.0
# pip3 install requests==2.23.*
# pip3 install requests==2.*
# pip3 uninstall requests

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

# for res in response:
print("hi", response.json())

# for now all the packages are installed globally, we can use different versions of packages for different applications



# ------------------------- Virtual Environment ---------------------------------
# install venv
# sudo apt install python3.10-venv

# for activitation the VE run
# source project1/bin/activate

# now install anything, and check the packages in site_packages file under lib folder.

# for deactivating, write deactivate in the terminal.

# ------------------------- Pipenv ---------------------------------
# it's a tool that combines pip and virtual environments into a single toolchain
# it's equallant to npm
# pip3 install pipenv
# adding the path in ~/.bashrc
# export PATH="$PATH:/home/ehmusman/.local/bin"
# source ~/.bashrc

# now install requests package with this command
# pipenv install requests
# now the virtual environment will not be in our directory

# pipenv --venv
# /home/ehmusman/.local/share/virtualenvs/python-E09BL5UR

# this is installed somewhere on machine, so that these packages should not be committed and pushed to github
