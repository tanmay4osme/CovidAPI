from flask import Flask
from flask import jsonify
import Indiacorona
app = Flask(__name__)
@app.route('/updates', methods=['GET'])
def upd():
    return jsonify(Indiacorona.est)


@app.route('/total', methods=['GET'])
def tot():
    return jsonify(Indiacorona.f)

@app.route('/')
def index():
    return jsonify(Indiacorona.d)
if __name__=="__main__":
    app.run(threaded=True, port=5000)
