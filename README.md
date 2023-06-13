# Extension Namer

[![PyPI version](https://badge.fury.io/py/extensionNamer.svg)](https://badge.fury.io/py/extensionNamer)
[![Downloads](https://pepy.tech/badge/extensionnamer)](https://pepy.tech/project/extensionNamer)

Python module that returns the name of an extension from a file path, extension or file name.

## Installation

```bash
pip install extensionNamer
```

## Usage

```python
from extensionNamer import extensionNamer

extensionNamer.getName("file.txt") # returns "Plain Text File"        

```

This module can used in cases like:

- **File Management**: You can use the script to automatically retrieve and display the full names of file extensions when managing files or working with file systems. This can be helpful when organizing, renaming, or categorizing files.

- **Data Processing**: If you're working with a large dataset that includes file extensions, the script can assist in providing meaningful information about each file extension. It can be used to enrich the dataset by adding the full names of the extensions for better analysis or reporting.

- **User Interfaces**: When building a user interface that involves file handling, you can incorporate the script to display user-friendly names for file extensions. This can enhance the user experience by providing clear and recognizable information about the files being accessed or manipulated.

- **File Conversion Tools**: If you're developing a file conversion tool, the script can help provide a user-friendly interface by displaying the full names of the source and target file extensions. This can assist users in selecting the appropriate file formats for conversion.

- **File Upload/Download Services**: When building a file upload or download service, the script can be utilized to display the full names of the uploaded or downloaded files. This can help users easily identify the file types they are working with.

These are just a few examples of how you can utilize a script that incorporates the extension name JSON file. The script can be customized and integrated into various applications or workflows depending on your specific needs.

## Contributing

If you want to contribute to this project, please read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
