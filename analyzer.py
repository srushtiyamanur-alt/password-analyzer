import math
import string

def check_length(password: str) -> bool:
    """Checks if password meets the minimum 8-character requirement."""
    return len(password) >= 8

def character_variety_score(password: str) -> int:
    """Scores password from 0 to 4 based on character types used."""
    score = 0
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    return score

def calculate_entropy(password: str) -> float:
    """Estimates password entropy in bits."""
    if not password:
        return 0.0
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += 32
    return round(len(password) * math.log2(pool), 2) if pool > 0 else 0.0
def strength_rating(password: str) -> str:
    """Classifies password strength as Weak, Moderate, or Strong."""
    if not check_length(password):
        return "Weak"
    score = character_variety_score(password)
    entropy = calculate_entropy(password)
    if score >= 3 and entropy >= 50:
        return "Strong"
    elif score >= 2 and entropy >= 35:
        return "Moderate"
    return "Weak"

if __name__ == "__main__":
    pwd = input("Enter a password to analyze: ")
    print(f"Meets length (>=8): {check_length(pwd)}")
    print(f"Variety Score (0-4): {character_variety_score(pwd)}")
    print(f"Estimated Entropy: {calculate_entropy(pwd)} bits")
