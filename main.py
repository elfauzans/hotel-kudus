from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/kamar')
def tipekamar(): 
    return render_template('kamar.html')

@app.route('/fasilitas')
def fasilitas(): 
    return render_template('fasilitas.html')

@app.route('/users')
def profile(): 
    return render_template('users.html')


if __name__ == '__main__':
    app.run(debug = True)