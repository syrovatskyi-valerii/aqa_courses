import uuid


def generate_random_email():

    unique_part = uuid.uuid4().hex[:6]
    return f"testuser_{unique_part}@mail.com"