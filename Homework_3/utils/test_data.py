import random

def generate_login():
    number = random.randint(1000, 900000)
    login = f"user_{number}"
    return login

def generate_age():
    age = random.randint(16, 90)
    return age

def generate_status():
    statuses = ["ACTIVE", "BLOCKED", "INACTIVE"]
    random_status = random.choice(statuses)
    return random_status

def generate_user():
    user = {
        "login": generate_login(),
        "age": generate_age(),
        "status": generate_status()
    }
    return user
