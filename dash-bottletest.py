import sendText
from bottle import route, run, template

@route('/hello')
def index():
    sendText

run(host='localhost', port=8080)
