import secrets
import string

def generate_password(Length: int = 16) -> str:
    strings = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(strings) for _ in range(Length))
    return password