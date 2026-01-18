# =========================
# CSRF Attack Simulation (Educational)
# =========================

# Simulated server state
USER_SESSION = {
    "authenticated": True,
    "csrf_token": "secure-random-token"
}

USER_BALANCE = 1000


# =========================
# Vulnerable server endpoint
# =========================
def transfer_money_vulnerable(amount):
    global USER_BALANCE
    if USER_SESSION["authenticated"]:
        USER_BALANCE -= amount
        print(f" Transfer successful! New balance: {USER_BALANCE}")
    else:
        print(" Not authenticated")


# =========================
# Protected server endpoint
# =========================
def transfer_money_protected(amount, csrf_token):
    global USER_BALANCE
    if not USER_SESSION["authenticated"]:
        print(" Not authenticated")
        return

    if csrf_token != USER_SESSION["csrf_token"]:
        print(" CSRF attack blocked!")
        return

    USER_BALANCE -= amount
    print(f" Transfer successful! New balance: {USER_BALANCE}")


# =========================
# Simulation
# =========================
if __name__ == "__main__":
    print("=== Initial balance ===")
    print(USER_BALANCE)

    print("\n=== Legitimate request (user action) ===")
    transfer_money_vulnerable(100)

    print("\n=== CSRF attack (malicious website) ===")
    transfer_money_vulnerable(300)

    print("\n=== Reset balance ===")
    USER_BALANCE = 1000
    print(USER_BALANCE)

    print("\n=== CSRF-protected request (legit) ===")
    transfer_money_protected(100, "secure-random-token")

    print("\n=== CSRF attack blocked ===")
    transfer_money_protected(300, "fake-token")
