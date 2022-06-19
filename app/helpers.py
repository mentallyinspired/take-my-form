import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check_email(email: str) -> bool:
    if(re.fullmatch(email_regex, email)):
        return True
    else:
        return False
    

def check_origin(origin: str, to_email: str):
    if not check_email(to_email):
        return False
    parts = to_email.split("@")
    domain = parts[1]
    if origin in domain:
        return True
    else:
        return False