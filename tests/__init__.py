import random
import string


def rnd_string():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(10))


def rnd_int():
    return random.randint(1, 99999)
