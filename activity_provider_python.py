from flask import Flask

Flask(__name__).get('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    Flask(__name__).run()