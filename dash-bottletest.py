import sendText
from bottle import route, run, template, request
number = "0"
@route('/hello')
def index():
    sendText

@route('/number')
def index():
	number = request.getone('number')
run(host='localhost', port=8080)
