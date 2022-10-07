import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def __repr__(self):
        return f'<User: {self.username}>'
    
    @staticmethod
    def validate_user(form):
        is_valid = True
        if not EMAIL_REGEX.match(form['email']):
            flash('Please enter a valid email address.')
            is_valid = False
        return is_valid