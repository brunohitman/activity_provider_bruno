# POST.py
from flask import Flask, jsonify
from post_command import PostCommand

app = Flask(__name__)

@app.route('/POST', methods=['POST'])
def post_example():
    post_command = PostCommand()
    return post_command.execute()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
