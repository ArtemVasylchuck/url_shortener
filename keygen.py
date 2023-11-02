import secrets
import string


def create_random_key(length: int = 5) -> str:
    chars = string.ascii_uppercase + string.digits
    return "".join([secrets.choice(chars) for _ in range(length)])


if __name__ == "__main__":
    print(create_random_key())