import secrets
import string


def generate_password(
    length=16,
    use_digits=True,
    use_symbols=True,
    use_uppercase=True,
    use_lowercase=True,
):
    """Generates a cryptographically secure random password."""
    # Ensure at least one character set is selected
    if not any([use_digits, use_symbols, use_uppercase, use_lowercase]):
        raise ValueError("At least one character type must be selected.")

    # Build character pool and ensure at least one character from each selected set
    character_pool = ""
    guaranteed_chars = []

    if use_lowercase:
        character_pool += string.ascii_lowercase
        guaranteed_chars.append(secrets.choice(string.ascii_lowercase))

    if use_uppercase:
        character_pool += string.ascii_uppercase
        guaranteed_chars.append(secrets.choice(string.ascii_uppercase))

    if use_digits:
        character_pool += string.digits
        guaranteed_chars.append(secrets.choice(string.digits))

    if use_symbols:
        # Common special characters
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        character_pool += symbols
        guaranteed_chars.append(secrets.choice(symbols))

    # Ensure length is long enough to hold guaranteed characters
    if length < len(guaranteed_chars):
        length = len(guaranteed_chars)

    # Fill the remaining slots randomly from the combined pool
    remaining_length = length - len(guaranteed_chars)
    remaining_chars = [
        secrets.choice(character_pool) for _ in range(remaining_length)
    ]

    # Combine and shuffle securely
    password_list = guaranteed_chars + remaining_chars
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)


# --- Example Usage ---
if __name__ == "__main__":
    # Generate a standard 16-character password
    password = generate_password(length=16)
    print(f"Generated Password: {password}")

    # Custom options (e.g., 20 characters, no symbols)
    alphanumeric_only = generate_password(
        length=20, use_symbols=False
    )
    print(f"Alphanumeric Password: {alphanumeric_only}")