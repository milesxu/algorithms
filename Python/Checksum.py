import hashlib


class checksum():

    """docstring for checksum"""

    def __init__(self):
        pass

    def sha256sum(self, filestr):
        file = open(filestr, "rb")
        sha256 = hashlib.sha256()
        sha256.update(file.read())
        return sha256.hexdigest()
