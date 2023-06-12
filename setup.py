from setuptools import setuptools, find_packages
from pathlib import Path

setuptools.setup(
    name="extensionNamer",
    version='{{VERSION_PLACEHOLDER}}',
    author="Deshy Dan",
    long_description=Path("README.md").read_text(),
    url = "https://github.com/DeshyDan/Extension-Namer",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"extensionNamer": ["extensionNamer/extensionNames.json"]}

)
