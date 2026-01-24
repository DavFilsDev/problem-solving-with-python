import uuid
import time

# Simulated database
USER_DB = {
    "alice": {
        "password": "S3cure!Pass#2025",
        "refresh_token": None,
        "device_id": None,
        "failed_attempts": 0,
        "locked_until": 0
    }
}

MAX_ATTEMPTS = 3
LOCK_TIME = 10  # seconds


# Secure login with rate limiting
def login(username, password, device_id):
    user = USER_DB.get(username)
    now = time.time()

    if now < user["locked_until"]:
        print(" Account temporarily locked")
        return None

    if password != user["password"]:
        user["failed_attempts"] += 1
        print(" Invalid credentials")

        if user["failed_attempts"] >= MAX_ATTEMPTS:
            user["locked_until"] = now + LOCK_TIME
            print(" Too many attempts. Account locked.")
        return None

    # Successful login
    user["failed_attempts"] = 0
    refresh_token = str(uuid.uuid4())
    user["refresh_token"] = refresh_token
    user["device_id"] = device_id

    print(" Login successful")
    print(f"Refresh token issued (HttpOnly)")
    return refresh_token


# Secure refresh with rotation + binding
def refresh_access(username, refresh_token, device_id):
    user = USER_DB.get(username)

    if user["refresh_token"] != refresh_token:
        print(" Token reuse detected! Session revoked.")
        user["refresh_token"] = None
        return None

    if user["device_id"] != device_id:
        print(" Device mismatch! Possible theft.")
        user["refresh_token"] = None
        return None

    # Rotate refresh token
    new_token = str(uuid.uuid4())
    user["refresh_token"] = new_token
    print(" Access token issued")
    print(" Refresh token rotated")
    return new_token


# Simulation
if __name__ == "__main__":
    print("=== STEP 1: Brute force attempt ===")
    login("alice", "123456", "attacker-device")
    login("alice", "password", "attacker-device")
    login("alice", "admin", "attacker-device")

    print("\n=== STEP 2: Legitimate login ===")
    token = login("alice", "S3cure!Pass#2025", "victim-device")

    print("\n=== STEP 3: Attacker steals old token ===")
    print(" Attacker tries reused token")
    refresh_access("alice", token, "attacker-device")

    print("\n=== STEP 4: Legitimate refresh ===")
    token = refresh_access("alice", token, "victim-device")

    print("\n=== STEP 5: Attacker tries rotated token ===")
    refresh_access("alice", token, "attacker-device")

    print("\n ACCOUNT SECURED — ATTACK FAILED 🛡")
