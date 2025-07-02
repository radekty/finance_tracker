# 📊 Finance Tracker

**Prosta aplikacja do śledzenia wydatków — stworzona w Pythonie z użyciem Flask, SQLite i Bootstrap.**

---

## 🚀 Funkcje

✅ Dodawanie wydatków (kwota, kategoria, data, opis)  
✅ Lista wszystkich wydatków w tabeli  
✅ Raport wydatków (z wykresami — wkrótce)  
✅ Prosty interfejs webowy  
✅ Gotowe do deployu (Heroku/Render)

---

## ⚙️ Technologie

- Python 3.x
- Flask
- SQLAlchemy (SQLite)
- Bootstrap 5
- Plotly (do wykresów)
- HTML, Jinja2

---

## 📂 Struktura projektu
finance_tracker/
├── app.py
├── models.py
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── add_expense.html
│ ├── report.html
├── static/
│ └── css/
│ └── style.css
├── expenses.db (tworzy się automatycznie)
├── .gitignore
├── requirements.txt

---

## 🚀 Jak uruchomić lokalnie

1️⃣ Sklonuj repo:
bash
git clone https://github.com/YOUR-USERNAME/finance-tracker.git
cd finance-tracker

2️⃣ Utwórz i aktywuj wirtualne środowisko:
bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

3️⃣ Zainstaluj zależności:
bash
pip install -r requirements.txt

4️⃣ Odpal aplikację:
bash
python app.py

5️⃣ Wejdź w przeglądarkę:
http://127.0.0.1:5000/

