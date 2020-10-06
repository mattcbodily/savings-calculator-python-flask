from flask import Flask
from flask import (render_template, request)
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def calculate_savings():
    if request.method == 'POST':
        product_name = request.form['product']
        product_price = float(request.form['price'])
        product_qty = int(request.form['quantity'])
        weekly_savings = product_price * product_qty * 7
        monthly_savings = product_price * product_qty * 30
        yearly_savings = product_price * product_qty * 365

        print(product_name)
        print(product_price)
        print(product_qty)

    return render_template('landing.html', weekly_savings=weekly_savings, monthly_savings=monthly_savings, yearly_savings=yearly_savings)