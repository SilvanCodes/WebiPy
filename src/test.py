#!/usr/bin/env python3

from inspect import signature
from flask import Flask, request
import json

PORT = 8081
app = Flask(__name__)

'''[[[cog
import cog
from inspect import signature

imported = __import__(IMPORT)

testInstance = getattr(imported, CLASS)

# inspect class
real_funcs = []
for func in dir(imported.TestClass):
  if func.startswith('__') and func.endswith('__'):
    # just a class function
    continue
  real_funcs.append(func)

cog.outl(f'from {IMPORT} import {CLASS}\n')
cog.outl(f'instance = {CLASS}()\n')

for func in real_funcs:
  cog.outl(f'@app.route(\'/{func}\')')
  cog.outl(f'def {func}():')
  sig = signature(getattr(testInstance, func))
  params = []
  for par in sig.parameters:
    if par == 'self':
      continue
    params.append(par)
    cog.outl(f'\t{par} = request.args.get(\'{par}\')')
  cog.outl(f"\treturn json.dumps(instance.{func}({', '.join(params)}))\n\n")
]]]'''
# [[[end]]]
if __name__ == '__main__':
  print('starting server....')
  app.run(debug=False, port=PORT)
