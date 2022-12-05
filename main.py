from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/create', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.values)
        return render_template('create.html')
    else:
        return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
