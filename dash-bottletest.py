import sendText
from bottle import route, run, template, request
number=""
message=""
@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='webpage/js')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='webpage/css')

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
