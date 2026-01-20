# =========================
# HttpOnly vs LocalStorage Attack Demo
# =========================

# Simulated browser storage
LOCAL_STORAGE = {
    "jwt": "JWT-SECRET-LOCALSTORAGE"
}

COOKIES = {
    "jwt": {
        "value": "JWT-SECRET-HTTPONLY",
        "httpOnly": True
    }
}

# =========================
# XSS payload simulation
# =========================
def xss_attack():
    print("\n XSS payload executed")

    # Steal LocalStorage token
    token = LOCAL_STORAGE.get("jwt")
    if token:
        print(f" Token stolen from LocalStorage: {token}")
        attacker_use_token(token)

    # Try to steal HttpOnly cookie
    cookie = COOKIES.get("jwt")
    if cookie and cookie["httpOnly"]:
        print(" HttpOnly cookie BLOCKED JS access")


# =========================
# Attacker uses token
# =========================
def attacker_use_token(token):
    print(f" Attacker authenticates using stolen token: {token}")
    print(" ACCOUNT TAKEOVER")


# =========================
# Simulation
# =========================
if __name__ == "__main__":
    print("=== LocalStorage scenario ===")
    xss_attack()

    print("\n=== HttpOnly Cookie scenario ===")
    print("JWT stored as HttpOnly cookie")
    xss_attack()
