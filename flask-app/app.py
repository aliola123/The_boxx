from flask import Flask
from flask import request, redirect, url_for, render_template
app = Flask(__name__, template_folder='templates')

def is_direct_url():
    referrer = request.referrer
    if referrer is None:
        return True
    return request.url_root not in referrer

@app.before_request
def check_direct_url():
    if is_direct_url() and request.path != '/':
        return render_template('error.html')
        
@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shop.html')
def shop():
    return render_template('shop.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/cart.html')
def cart():
    return render_template('cart.html')

@app.route('/pdesc.html')
def pdesc():
    return render_template('pdesc.html')

if __name__ == '__main__':
    app.run(debug=True)

