import string
import random


def get_password(count_digits: int
                 , count_ascii_letters: int
                 , case_sensitive=False) -> str:
    password = ''.join(random.sample(string.digits, count_digits))
    letters = string.ascii_lowercase

    if case_sensitive:
        letters += string.ascii_uppercase

    password += ''.join(random.sample(letters, count_ascii_letters))
    password = ''.join(random.sample(password, len(password)))

    return password


if __name__ == '__main__':
    pass
