import json
import os


def _loadExtensionNames():
    """
     Load the list of extension names. This is a private function and should not be called outside of this module.

     @return A list of extension
    """
    with open("extensionNamer/extensionNames.json") as f:
        extensionNames = json.load(f)
    return extensionNames


def getName(extension):
    """
     Returns the name of the extension. If the extension is not found in the list of extensions, " Unknown " is returned.


     @param extension - The extension to get the name of. This can be a file path or just the extension itself.

     @return The name of the extension or " Unknown " if not found in the list of extensions or the extension does not exist.
    """
    extensionNames = _loadExtensionNames()
    # Returns the name of the file extension.
    if os.path.isfile(extension):
        extension = os.path.splitext(extension)[1]
        return extensionNames[extension]

    elif extension in extensionNames:
        return extensionNames[extension]
    else:
        return "Unknown"
