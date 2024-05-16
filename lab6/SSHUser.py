from datetime import datetime
import re

class SSHUser:
    def __init__(self, username, last_login=datetime.now()):
        self.username = username
        self.last_login = last_login

    def __str__(self):
        return f"User: {self.username}, last login: {self.last_login}"

    def validate(self):

        #zalezy od zalozenia wiec zostaiam do szybkiej zmiany
        if self.username is None:
            return False

        return re.match(r'^[a-z_][a-z0-9_-]{0,31}$', self.username) is not None and self.username != 'user'