from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = {
        "welcome": "it works"
    }
    return jsonify(data)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 