from setuptools import setuptools, find_packages
from pathlib import Path

setuptools.setup(
    name="extensionNamer",
    version="1.0.0",
    author="Deshy Dan",
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"extensionNamer": ["extensionNamer/extensionNames.json"]}

)
