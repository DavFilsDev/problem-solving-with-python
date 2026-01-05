import hashlib

def crack(hash):
    for i in range(100000):
        pin = f"{i:05d}"
        if hashlib.md5(pin.encode()).hexdigest() == hash:
            return pin
