# highly related things shold be at same place

# multiple ways of import

# 01
from ecommerace.shipping.sales import calculate_shippment, calculate_tax

# 02

import ecommerace.products

# 03
from ecommerace.shipping import sales

calculate_shippment()
calculate_tax()

sales.calculate_shippment()
sales.calculate_tax()

ecommerace.products.get_products()
ecommerace.products.remove_product()



# ------------------------------ Compiling python files  ------------------------

# when we'll run python3 app.py, a new folder will be created named as __pycache__. this will have compiled version of all different files. new time python will import the module faster and python update these cashed files automatically based on the timestamp app.py and any module.
# this will only faster the module import, the execution time will be same



# ------------------------------ Module searches  ------------------------
# import sales

# # against above line, python search the modules in following files
# import sys
# print(sys.path)
# """
# ['/home/ehmusman/Desktop/usman/python/07-modules', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']
# """


# ------------------------------ Packages   ------------------------
# when we need to import file from a subdirectory
# add a new file in the subdirectory named as __init__.py
# python will treat that folder as a package. a package is a container of one or more modules.
# in file system terms, a package is not a directoy, a module is not a file.
# now we need to perefix the module with directory/folder_name


# ------------------------------ Sub Packages   ------------------------
# we need to prefix the package name with sub directory name, like

# from ecommerace.shipping.sales import calculate_shippment, calculate_tax
# from ecommerace.shipping import sales


# ------------------------------ Intra Package Reference   ------------------------
# Importing module from sibling packages
#  we can use absolute or relative import

# Absolute import
# from ecommerace.shipping import sales
# sales.calculate_shippment()


# Relative import
# from ..shipping import sales
# sales.calculate_tax()


# ------------------------------ dir function   ------------------------
# this built in function is used to get the names of all the methods available in a module. this is mostly used for debugging

# print(dir(sales))
# print(sales.__doc__)
# print(sales.__file__)
# print(sales.__name__)
# print(sales.__package__)
# there are some builtin magic methods for us. all are printed
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calculate_shippment', 'calculate_tax']


# ------------------------------ Executing module as a script   ------------------------

# if we'll run the module as a script, the __name__ will be __main__. based on this flag, we can do some executions like