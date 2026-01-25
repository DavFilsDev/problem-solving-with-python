# Token Binding to Device/IP Demo

import uuid

# Simulated database
SESSIONS = {}

# Login (issue bound token)
def login(user, device_id, ip):
    refresh_token = str(uuid.uuid4())
    SESSIONS[refresh_token] = {
        "user": user,
        "device_id": device_id,
        "ip": ip
    }

    print(f" Login successful")
    print(f"Refresh token: {refresh_token}")
    print(f"Bound to device: {device_id}")
    print(f"Bound to IP: {ip}")
    return refresh_token


# Refresh access token
def refresh_access(refresh_token, device_id, ip):
    session = SESSIONS.get(refresh_token)

    if not session:
        print(" Invalid refresh token")
        return

    if session["device_id"] != device_id:
        print(" Device mismatch! Possible token theft.")
        return

    if session["ip"] != ip:
        print(" IP mismatch! Possible token theft.")
        return

    print(" Access token issued successfully")


# Simulation
if __name__ == "__main__":
    print("=== Legitimate login ===")
    token = login(
        user="alice",
        device_id="device-123",
        ip="192.168.1.10"
    )

    print("\n=== Legitimate refresh ===")
    refresh_access(
        refresh_token=token,
        device_id="device-123",
        ip="192.168.1.10"
    )

    print("\n=== Attacker steals token ===")
    refresh_access(
        refresh_token=token,
        device_id="attacker-device",
        ip="203.0.113.99"
    )
