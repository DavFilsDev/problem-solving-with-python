import time
import hmac

SECRET = "superSecret123"

# Insecure comparison (vulnerable to timing attacks)
def insecure_compare(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False

    for x, y in zip(a, b):
        if x != y:
            return False
        time.sleep(0.01)  # simulate processing delay

    return True


# Secure comparison (constant-time)
def secure_compare(a: str, b: str) -> bool:
    return hmac.compare_digest(a, b)


def measure(func, guess: str, rounds=5):
    total = 0.0
    for _ in range(rounds):
        start = time.perf_counter()
        func(guess, SECRET)
        end = time.perf_counter()
        total += (end - start)
    return total / rounds


if __name__ == "__main__":
    guesses = [
        "x",
        "s",
        "su",
        "sup",
        "super",
        "superS",
        "superSecret123",
    ]

    print(" Timing attack demonstration\n")

    print(" Insecure comparison:")
    for g in guesses:
        t = measure(insecure_compare, g)
        print(f"Guess: {g:<20} Time: {t:.5f} seconds")

    print("\n Secure comparison:")
    for g in guesses:
        t = measure(secure_compare, g)
        print(f"Guess: {g:<20} Time: {t:.5f} seconds")
