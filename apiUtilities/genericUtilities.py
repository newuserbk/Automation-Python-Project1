import random
import string


def generate_random_email_and_password(domain=None, email_prefix=None):
    if not domain:
        domain = 'sdfh.com'
    if not email_prefix:
        email_prefix = 'tesuser'

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
