import secrets
import string


def generate_password(length):
    """Generate a secure random password."""

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_characters = lowercase + uppercase + digits + symbols

    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Shuffle securely
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def evaluate_strength(password):
    """Evaluate password strength."""

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"


def main():
    print("=" * 40)
    print("      Secure Password Generator")
    print("=" * 40)

    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("Password length must be at least 8 characters.\n")
                continue

            break

        except ValueError:
            print("Please enter a valid number.\n")

    password = generate_password(length)
    strength = evaluate_strength(password)

    print("\nGenerated Password:")
    print(password)

    print(f"\nPassword Strength: {strength}")


if __name__ == "__main__":
    main()