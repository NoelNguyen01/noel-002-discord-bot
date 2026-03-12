# Utility functions and helper methods

def current_datetime_utc():
    """Returns the current date and time in UTC as a formatted string."""
    from datetime import datetime
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


def greet_user(username):
    """Greets the user with a friendly message."""
    return f'Hello, {username}! Welcome to the Utility functions.'


# Example usage:
# print(current_datetime_utc())
# print(greet_user('User'))