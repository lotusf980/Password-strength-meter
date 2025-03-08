import re
import random
import string
import streamlit as st

# Common weak passwords to blacklist
BLACKLIST = {"password", "123456", "12345678", "qwerty", "abc123", "password123", "111111"}

def check_password_strength(password):
    """Check the strength of a password and return feedback."""
    score = 0
    feedback = []

    # Check if password is blacklisted
    if password.lower() in BLACKLIST:
        return "❌ This password is too common. Choose a stronger one."

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!"
    elif score == 3:
        return "⚠ Moderate Password - Consider adding more security features."
    else:
        return "❌ Weak Password - Improve it using the suggestions below:\n" + "\n".join(feedback)

def generate_password(length=12):
    """Generate a strong random password."""
    if length < 8:
        return "⚠ Password length should be at least 8 characters."

    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))

    return password

# Streamlit GUI
st.title("🔑 Password Strength Meter")

password = st.text_input("Enter a password", type="password")

if st.button("Check Strength"):
    if password:
        result = check_password_strength(password)
        st.write(result)
    else:
        st.warning("Please enter a password.")

if st.button("Generate Strong Password"):
    strong_password = generate_password()
    st.success(f"Generated Password: {strong_password}")