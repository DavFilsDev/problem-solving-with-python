import time

# Simulated database
REAL_PASSWORD = "admin123"

# Insecure login (no protection)
def insecure_login(password: str) -> bool:
    return password == REAL_PASSWORD


# Secure login with rate limiting
attempts = {}
MAX_ATTEMPTS = 3
BLOCK_TIME = 5  # seconds

def secure_login(password: str, user_id="attacker") -> bool:
    current_time = time.time()

    if user_id in attempts:
        count, last_time = attempts[user_id]

        # Block user temporarily
        if count >= MAX_ATTEMPTS and current_time - last_time < BLOCK_TIME:
            print(" Too many attempts. Try again later.")
            return False

        # Reset after block time
        if current_time - last_time >= BLOCK_TIME:
            attempts[user_id] = (0, current_time)

    # Check password
    if password == REAL_PASSWORD:
        print(" Login successful")
        attempts[user_id] = (0, current_time)
        return True
    else:
        count, _ = attempts.get(user_id, (0, current_time))
        attempts[user_id] = (count + 1, current_time)
        print(f" Login failed ({attempts[user_id][0]} attempts)")
        return False


# Attack simulation
if __name__ == "__main__":
    password_list = [
        "123456",
        "password",
        "admin",
        "admin123",  # correct password
    ]

    print("\n Brute force WITHOUT rate limiting\n")
    for pwd in password_list:
        print(f"Trying: {pwd}")
        if insecure_login(pwd):
            print(" Password found!\n")
            break

    print("\n🛡 Brute force WITH rate limiting\n")
    for pwd in password_list:
        print(f"Trying: {pwd}")
        secure_login(pwd)
        time.sleep(1)
