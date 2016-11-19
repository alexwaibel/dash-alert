from bottle import route, run, template

@route('/hello')
def index():
    print("worked")

run(host='localhost', port=8080)
