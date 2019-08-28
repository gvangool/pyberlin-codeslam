#!/usr/bin/env python3
import string

alphabet = string.ascii_letters + string.digits

# Don't do this
def generate_password(length):
    import random

    return "".join(
        alphabet[random.randint(0, len(alphabet) - 1)] for _ in range(length)
    )


print(f"{generate_password(8)=}")


# But do this (https://docs.python.org/3/library/secrets.html)
def generate_password_secure(length):
    import secrets

    return "".join(secrets.choice(alphabet) for _ in range(length))


print(f"{generate_password_secure(8)=}")
