import ast
src=open('genpains.py',encoding='utf-8').read()
try:
    ast.parse(src); print('parses OK')
except SyntaxError as e:
    print('SYNTAX', e.lineno, e.msg)
