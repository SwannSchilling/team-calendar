import ast
try:
    ast.parse(open('genpains.py',encoding='utf-8').read()); print('parses OK')
except SyntaxError as e:
    print('SYNTAX', e.lineno, e.msg)
