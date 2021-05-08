from flask import Flask
app = Flask(__name__)

@app.route('/a')
def hello_world1():
    return 'Hello!'

@app.route('/b')
def hello_world2():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()