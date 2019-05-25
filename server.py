from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
	return 'PONG'

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5050)

