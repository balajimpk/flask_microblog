import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_own_key_that_cannot_be_guessed'