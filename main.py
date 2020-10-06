from flask import Flask
from flask import (render_template, request)
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def calculate_savings():
    if request.method == 'POST':
        product_name = request.form['product']
        product_price = request.form['price']
        product_qty = request.form['quantity']

        print(product_name)
        print(product_price)
        print(product_qty)

    return render_template('landing.html')