from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    yes = ''
    for i in range(parameter):
        yes += f'{i}\n'
    return yes

@app.route('/math/<int:num1><op><int:num2>')
def math(num1, op, num2):
    yes = 0
    if (op == '+'):
        yes = num1 + num2
    elif (op == '-'):
        yes = num1 - num2
    elif (op == '*'):
        yes = num1 * num2
    elif (op == 'div'):
        yes = num1 / num2
    elif (op == '%'):
        yes = num1 % num2
    else:
        yes = 'NO!'
    print(yes)
    return f'{yes}'