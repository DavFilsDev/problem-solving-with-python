# Stored XSS -> Full Takeover Demo

# Simulated database
COMMENTS_DB = []
SESSIONS = {
    "victim_session": "JWT-VICTIM-SECRET"
}

# Vulnerable comment storage
def store_comment_vulnerable(comment):
    COMMENTS_DB.append(comment)
    print(" Comment stored (NO sanitization)")


# Page rendering (vulnerable)
def render_page_vulnerable():
    print("\n Rendering page...")
    for c in COMMENTS_DB:
        print(f"Rendered comment: {c}")
        if "<script>" in c:
            steal_token()


# XSS payload effect
def steal_token():
    stolen = SESSIONS["victim_session"]
    print(f" XSS executed! Token stolen: {stolen}")
    attacker_use_token(stolen)


# Attacker uses stolen token
def attacker_use_token(token):
    print(f" Attacker uses stolen token: {token}")
    print(" FULL ACCOUNT TAKEOVER")


# Secure comment storage
def store_comment_secure(comment):
    safe = comment.replace("<", "&lt;").replace(">", "&gt;")
    COMMENTS_DB.append(safe)
    print(" Comment stored (sanitized)")


# Secure rendering
def render_page_secure():
    print("\n Rendering page (secure)...")
    for c in COMMENTS_DB:
        print(f"Rendered comment: {c}")


# Simulation
if __name__ == "__main__":
    print("=== STORED XSS ATTACK ===")
    store_comment_vulnerable("<script>steal()</script>")
    render_page_vulnerable()

    print("\n=== FIXED VERSION ===")
    COMMENTS_DB.clear()
    store_comment_secure("<script>steal()</script>")
    render_page_secure()
