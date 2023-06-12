import tarfile

tar = tarfile.open("dist/extensionNamer-1.0.9.tar.gz", "r:gz")
print(tar.getnames())