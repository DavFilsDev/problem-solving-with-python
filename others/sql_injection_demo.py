import sqlite3

# =========================
# Database setup
# =========================
def setup_db():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE users (
            username TEXT,
            password TEXT
        )
    """)

    cursor.execute("INSERT INTO users VALUES ('admin', 'admin123')")
    cursor.execute("INSERT INTO users VALUES ('user', 'password')")

    conn.commit()
    return conn


# =========================
# Vulnerable login (SQL Injection)
# =========================
def vulnerable_login(conn, username, password):
    cursor = conn.cursor()

    query = f"""
        SELECT * FROM users
        WHERE username = '{username}'
        AND password = '{password}'
    """

    print(f"\n[DEBUG] Executed query:\n{query}")

    cursor.execute(query)
    return cursor.fetchone() is not None


# =========================
# Secure login (Parameterized query)
# =========================
def secure_login(conn, username, password):
    cursor = conn.cursor()

    query = """
        SELECT * FROM users
        WHERE username = ?
        AND password = ?
    """

    cursor.execute(query, (username, password))
    return cursor.fetchone() is not None


# =========================
# Demo
# =========================
if __name__ == "__main__":
    conn = setup_db()

    print("🔓 NORMAL LOGIN (vulnerable)")
    print(vulnerable_login(conn, "admin", "admin123"))

    print("\n💣 SQL INJECTION ATTEMPT")
    injected_password = "' OR '1'='1"
    print(vulnerable_login(conn, "admin", injected_password))

    print("\n🛡 SECURE LOGIN WITH SAME INPUT")
    print(secure_login(conn, "admin", injected_password))
