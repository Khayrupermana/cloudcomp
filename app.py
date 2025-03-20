from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return f"Received: Name={name}, Email={email}"
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Email: <input type="text" name="email"><br>
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
