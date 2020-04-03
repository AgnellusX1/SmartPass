from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('MLpg.html')

# @app.route('/generate')
# def generate():
#     return render_template('process.html')


# @app.route('/',methods=[POST])
# def getvalue():
#     if request.method == 'POST':

#         name = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         return render_template('MLpg.html', u=name , e = email , p = password)

if __name__ == '__main__':
    app.run(debug=True)
