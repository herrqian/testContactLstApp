import time

# test constants for signup
valid_credentials = [
    {
        "FIRST_NAME": "ADAMS",
        "LAST_NAME": "SMITH",
        "EMAIL": f"{time.time().hex()}@123.de",
        "PASSWORD": "12345678",
    },
]

invalid_credentials = [
    {
        "FIRST_NAME": "ADAMS",
        "LAST_NAME": "SMITH",
        "EMAIL": "abc@123.de",
        "PASSWORD": "1234",
    },
    {
        "FIRST_NAME": "TOM",
        "LAST_NAME": "MILLER",
        "EMAIL": "abc123",
        "PASSWORD": "12341234",
    }
]

# sign in constants
login_data = [
    (
        "321@123.com",
        "12345678",
        "SUCCEED",
    ),
    (
        "321@123.com",
        "1234",
        "FAILED",
    ),
]