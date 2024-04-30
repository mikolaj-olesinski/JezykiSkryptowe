from datetime import datetime
import re

class SSHUser:
    def __init__(self, username, last_login):
        self.username = username
        self.last_login = last_login

    def __init__(self, username):
        self.username = username
        self.last_login = datetime.now()

    def __str__(self):
        return f"User: {self.username}, last login: {self.last_login}"

    def validate(self):
        return re.match(r'^[a-z_][a-z0-9_-]{0,31}$', self.username) is not None and self.username != 'user'