from flask import Flask, render_template, request, redirect, url_for
from models import db, Expense
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    expenses = Expense.query.all()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        category = request.form['category']
        description = request.form['description']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')

        new_expense = Expense(amount=amount, category=category, description=description, date=date)
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_expense.html')

@app.route('/report')
def report():
    expenses = Expense.query.all()
    total_amount = sum(expense.amount for expense in expenses)
    return render_template('report.html', expenses=expenses, total_amount=total_amount)

if __name__ == '__main__':
    app.run(debug=True)