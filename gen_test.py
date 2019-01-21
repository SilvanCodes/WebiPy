#!/usr/bin/env python3

from inspect import signature
from flask import Flask, request
import json

PORT = 8081
app = Flask(__name__)

from test_class import TestClass

instance = TestClass()

@app.route('/add')
def add():
	a = request.args.get('a')
	b = request.args.get('b')
	return json.dumps(instance.add(a, b))


@app.route('/reply')
def reply():
	text = request.args.get('text')
	return json.dumps(instance.reply(text))


if __name__ == '__main__':
  print('starting server....')
  app.run(debug=False, port=PORT)
