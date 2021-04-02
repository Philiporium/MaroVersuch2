from flask import *
app = Flask(__name__)

@app.route('/')
def start():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/About.html')
def about():
    return render_template('About.html')

@app.route('/contactUs.html')
def contact():
    return render_template('contactUs.html')

@app.route('/products.html')
def products():
    return render_template('products.html')

@app.route('/services.html')
def services():
    return render_template('services.html')