from flask import Flask
app = Flask(__name__)
 
from flask import jsonify, abort, request, make_response
from hashlib import md5
import os
 
SecretKey = 'Qi3mnN9b3UougbpqFvsGruSir0tKPlhc'
ALLOW_LIST = ['nduytg','cloudcraft']
COMMAND = 'echo Hello World'
 
@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.6 (from the example template)"
 
#### Task API ####
@app.route('/api')
def index():
    abort(403)
 
# Run a custom task on server when receiving POST request
@app.route('/api/tasks', methods=['POST'])
def runTask():
    data = request.form.to_dict()
 
    if len(data) == 0:
        abort(403)
    if data['user'] not in ALLOW_LIST:
        abort(403)
 
    # sign = md5(time + user + SecretKey)
    serverSign = md5((data['time'] + data['user'] + SecretKey).encode('utf-8')).hexdigest()
 
    if serverSign == data['sign']:
        # Run script
        #print('Do something')
        result = os.system(COMMAND)
 
        if result == 0:
            return  make_response(jsonify({'Result code': 0, 'Message':'Run task successfully'})) 
        else:
            return  make_response(jsonify({'Result code': -1, 'Message':'Task failed! Try again'})) 
    else:
        return make_response(jsonify({'Error code': -1, 'Error message':'Wrong Paramters'})) 
 
# Error Handlers
@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'Error code': 404, 'Error message':'Not found'}))
 
@app.errorhandler(403)
def permissionDenied(error):
    return make_response(jsonify({'Error code': 403, 'Error message':'Permission Denied'}))
 
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=5000)