# JWT CSRF Vulnerability Demo

# Simulated server state
USER_SESSION = {
    "jwt_cookie": "jwt-token-123",  # stored in cookie
    "csrf_token": "csrf-secure-token"
}

USER_BALANCE = 1000


# Vulnerable JWT endpoint
def transfer_vulnerable(amount, jwt_cookie):
    global USER_BALANCE

    if jwt_cookie == USER_SESSION["jwt_cookie"]:
        USER_BALANCE -= amount
        print(f" Transfer OK (JWT accepted). Balance: {USER_BALANCE}")
    else:
        print(" Unauthorized")


# Secure JWT endpoint
def transfer_secure(amount, jwt_cookie, csrf_token):
    global USER_BALANCE

    if jwt_cookie != USER_SESSION["jwt_cookie"]:
        print(" Unauthorized")
        return

    if csrf_token != USER_SESSION["csrf_token"]:
        print(" CSRF blocked!")
        return

    USER_BALANCE -= amount
    print(f"💸 Secure transfer OK. Balance: {USER_BALANCE}")


# Simulation
if __name__ == "__main__":
    print("=== Initial balance ===")
    print(USER_BALANCE)

    print("\n=== Legitimate request ===")
    transfer_vulnerable(100, "jwt-token-123")

    print("\n=== CSRF attack (browser sends JWT automatically) ===")
    transfer_vulnerable(300, "jwt-token-123")

    print("\n=== Reset balance ===")
    USER_BALANCE = 1000
    print(USER_BALANCE)

    print("\n=== Legitimate secure request ===")
    transfer_secure(100, "jwt-token-123", "csrf-secure-token")

    print("\n=== CSRF attack blocked ===")
    transfer_secure(300, "jwt-token-123", "fake-token")
