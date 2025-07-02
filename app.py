from flask import Flask, render_template, request, redirect, url_for
from models import db, Expense
from datetime import datetime
import pandas as pd
import plotly.express as px

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

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/report')
def report():
    expenses = Expense.query.all()
    if not expenses:
        return render_template('report.html', plot_div=None)
    
    data = [{
        'Amount': expense.amount,
        'Category': expense.category
    } for expense in expenses]
    
    df = pd.DataFrame(data)

    fig = px.pie(df, names='Category', values='Amount', title='Wydatki według kategorii')

    plot_div = fig.to_html(full_html=False)

    return render_template('report.html', plot_div=plot_div)

if __name__ == '__main__':
    app.run(debug=True)