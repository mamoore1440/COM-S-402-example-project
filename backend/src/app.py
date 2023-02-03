from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/post', methods=["POST"])
def testpost():
    input_json = request.get_json(force=True) 
    dictToReturn = {'text': input_json['text']}
    return jsonify(dictToReturn)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')
