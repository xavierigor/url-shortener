import string
from random import choice


def generate_random_string(size=6, chars=string.ascii_lowercase + string.digits):
    """
    Generates random string with numbers and letters
    """
    return ''.join(choice(chars) for _ in range(size))
