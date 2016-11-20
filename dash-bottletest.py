import sendText
from bottle import route, run, template, request
number=""
message=""
@route('/')
def index():
	indexStr = open("webpage/index.html","r").read()
	return template(indexStr)

@route('/add',method='POST')
def index():
	global number
	global message
	number=request.forms.get('number')
	message=request.forms.get('message')

@route('/hello')
def index():
	global number
	global message
	sendText.sendItOutPlz(number,message)


run(host='localhost', port=8080)
