import hashlib
import os


SIZE = 64


def myhash(m):
    #Generate random nonce
    nonce = os.urandom(SIZE)
    #Generate hex digest
    h_hex = hashlib.sha256(nonce + m.encode('utf-8')).hexdigest()
    return nonce, h_hex



