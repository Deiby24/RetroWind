from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html' , static_url=app.static_url_path)

@app.route('/cart')
def cart():
    return render_template('cart.html')

# def inject_static_url():
#     def static_url(filename):
#         return url_for('static', filename=filename)
#     return dict(static_url=static_url)

if __name__ == '__main__':
    app.run(debug=True)