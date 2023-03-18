from setuptools import setup, find_packages

setup(
    name = "src",
    version= "0.0.1",
    author= "tiksharsh",
    description= "mlOps-WinQ",
    packages= find_packages(),
    license= "MIT"
)

# pip install -e .

# to chk all installed packages
# pip freeze

# run below cmd and then you can share distribution with frnds and others (chk inside dist folder)
# python setup.py sdist bdist_wheel
