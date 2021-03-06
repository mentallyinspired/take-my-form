import re, json, os, configparser, shutil

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check_email(email: str) -> bool:
    """Check if email is valid

    Args:
        email (str): email address

    Returns:
        bool: True if valid, false otherwise
    """
    if(re.fullmatch(email_regex, email)):
        return True
    else:
        return False
    

def check_origin(origin_url: str, ALLOWED_URLS: list) -> bool:
    """Check that the origin domain is in our list

    Args:
        request (Request): HTTP request, for origin url
        ALLOWED_URLS (list): List of allowed urls

    Returns:
        bool: True if origin url in list, otherwise False
    """
    if origin_url == None:
        origin_url = "https://invalid.invalid"
    
    if not origin_url in ALLOWED_URLS:
        return False
    else:
        return True
    

def get_allowed_origins() -> list:
    """Read from config and return a list of allowed domains.

    Returns:
        list: List of allowed items
    """
    config = configparser.ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), "config", "config.ini")
    config.read(config_file)
    urls = config['SMTP']['ALLOWED_URLS']
    allowed_urls = json.loads(urls)
    return allowed_urls


def create_config_file():
    """Check for config.ini in config dir, copy it over if it isn't there.
    """
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "config", "config.ini")):
        original = os.path.join(os.path.dirname(__file__), "config.ini")
        target = os.path.join(os.path.dirname(__file__), "config", "config.ini")
        shutil.copyfile(original, target)