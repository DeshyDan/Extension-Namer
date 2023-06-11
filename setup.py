import setuptools
from pathlib import Path

setuptools.setup(
    name="extensionNamer",
    version="1.0.0",
    long_description=Path("README.md").read_text(),
    pakages=setuptools.find_packages()
)
