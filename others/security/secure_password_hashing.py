import hashlib
import hmac


def hash_password(password: str) -> str:
    """
    Hash a password using SHA-256
    """
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, stored_hash: str) -> bool:
    """
    Securely compare password hash with stored hash
    """
    password_hash = hash_password(password)
    return hmac.compare_digest(password_hash, stored_hash)


def run_tests():
    print("=== PASSWORD HASHING TEST ===")

    password = "securePassword123"
    wrong_password = "wrongPassword"

    stored_hash = hash_password(password)

    print("Correct password:",
          verify_password(password, stored_hash),
          "→ expected True")

    print("Wrong password:",
          verify_password(wrong_password, stored_hash),
          "→ expected False")


if __name__ == "__main__":
    run_tests()
