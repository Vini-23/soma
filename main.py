
# ------------------- IMPORTANDO PACOTES -------------------

from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.secret_key = 'calculate'

# ------------------- CÓDIGO DA APLICAÇÃO -------------------

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = None

    if request.method == 'POST':
        number_1 = int(request.form['number_1']) 
        number_2 = int(request.form['number_2'])
        operation = request.form['operation']

        if operation == 'mais':
            result = number_1 + number_2
            operation = '+'
        elif operation == 'menos':
            result = number_1 - number_2
            operation = '-'
        elif operation == 'vezes':
            result = number_1 * number_2
            operation = 'x'
        else:
            if number_2 == 0:
                result = 'Error: Divisão por zero'
                flash('Não é possível dividir um número por 0. Selecione outro número.')
            else:
                result = number_1 / number_2
                operation = '÷'

        if result == 'Error: Divisão por zero':
            return render_template('index.html', result=None)

        return render_template('index.html', number_1=number_1, number_2=number_2, operation=operation, result=result)

    return render_template('index.html', result=result)


# ------------------- RODANDO A APLICAÇÃO -------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)