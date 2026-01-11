def alphanumeric(password: str) -> bool:
    return password.isalnum()

tests = [
    "abc123",
    "ABC",
    "123",
    "",
    "abc_123",
    "abc 123",
    "abc!"
]

for t in tests:
    print(t, "=>", alphanumeric(t))
