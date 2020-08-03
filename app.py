from flask import Flask, jsonify


app = Flask(__name__)

data =  {
            "id": 1,
            "frameworks": "Django",
            "year": 2005
        }


@app.route('/')
def home():
    return "Hello World"


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)  # Return web frameworks information

if __name__ == '__main__':
    app.run(host='0.0.0.0')
