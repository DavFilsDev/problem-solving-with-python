import hashlib
import bcrypt

# Dictionary of common passwords
PASSWORD_LIST = [
    "123456",
    "password",
    "admin",
    "qwerty",
    "letmein",
    "welcome",
    "admin123"
]

# Weak hashing (MD5) - BAD
def md5_hash(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

# Strong hashing (bcrypt) - GOOD
def bcrypt_hash(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Dictionary attack on MD5
def dictionary_attack_md5(target_hash):
    print("\n Starting dictionary attack on MD5 hash...")

    for pwd in PASSWORD_LIST:
        hashed = md5_hash(pwd)
        print(f"Trying {pwd} → {hashed}")

        if hashed == target_hash:
            print(f"\n Password cracked: {pwd}")
            return pwd

    print("\n Password not found")
    return None

# Dictionary attack on bcrypt (fails)
def dictionary_attack_bcrypt(target_hash):
    print("\n Starting dictionary attack on bcrypt hash...")

    for pwd in PASSWORD_LIST:
        if bcrypt.checkpw(pwd.encode(), target_hash):
            print(f"\n Password cracked: {pwd}")
            return pwd
        else:
            print(f"Trying {pwd} → no match")

    print("\n Password not found")
    return None


# Demo
if __name__ == "__main__":
    real_password = "admin123"

    print("=== Weak password stored with MD5 ===")
    md5_stored = md5_hash(real_password)
    print(f"Stored hash: {md5_stored}")

    dictionary_attack_md5(md5_stored)

    print("\n=== Same password stored with bcrypt ===")
    bcrypt_stored = bcrypt_hash(real_password)
    print(f"Stored hash: {bcrypt_stored}")

    dictionary_attack_bcrypt(bcrypt_stored)
