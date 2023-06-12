import json
import os


def _loadExtensionNames():
    """
     Load the list of extension names. This is a private function and should not be called outside of this module.

     @return A list of extension
    """
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'extensionNames.json')
    with open(file_path, 'r') as jfile:
        extensionNames = json.load(jfile)
    return extensionNames


def getName(extension):
    """
    Returns the name of the extension. If the extension is not found in the list of extensions, "Unknown" is returned.

    @param extension - The extension to get the name of. This can be a file path or just the extension itself.

    @return The name of the extension or "Unknown" if not found in the list of extensions.
    """
    extensionNames = _loadExtensionNames()
    extension = os.path.splitext(extension)[1]  
    return extensionNames.get(extension, "Unknown")

