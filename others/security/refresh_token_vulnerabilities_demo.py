# Refresh Token Vulnerability Demo

import uuid

# Simulated database
USER_DB = {
    "user1": {
        "refresh_token": None
    }
}

# Vulnerable implementation
def login_vulnerable(user):
    refresh_token = str(uuid.uuid4())
    USER_DB[user]["refresh_token"] = refresh_token
    print(f" Login OK. Refresh token issued: {refresh_token}")
    return refresh_token


def refresh_access_vulnerable(user, refresh_token):
    if USER_DB[user]["refresh_token"] == refresh_token:
        print(" New access token issued")
        return True
    else:
        print(" Invalid refresh token")
        return False


# Secure implementation (rotation)
def login_secure(user):
    refresh_token = str(uuid.uuid4())
    USER_DB[user]["refresh_token"] = refresh_token
    print(f" Login OK. Refresh token issued: {refresh_token}")
    return refresh_token


def refresh_access_secure(user, refresh_token):
    if USER_DB[user]["refresh_token"] != refresh_token:
        print(" Refresh token reuse detected! Session revoked.")
        USER_DB[user]["refresh_token"] = None
        return False

    new_refresh_token = str(uuid.uuid4())
    USER_DB[user]["refresh_token"] = new_refresh_token
    print(" New access token issued")
    print(f" Refresh token rotated: {new_refresh_token}")
    return new_refresh_token


# Simulation
if __name__ == "__main__":
    print("=== Vulnerable Flow ===")
    rt = login_vulnerable("user1")

    print("\nAttacker steals refresh token...")
    refresh_access_vulnerable("user1", rt)
    refresh_access_vulnerable("user1", rt)  # reuse works XXXXX

    print("\n=== Secure Flow ===")
    rt = login_secure("user1")

    print("\nLegitimate refresh")
    rt = refresh_access_secure("user1", rt)

    print("\nAttacker tries reused token")
    refresh_access_secure("user1", rt)  # fails XXXXX
