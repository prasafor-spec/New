from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            mobile TEXT NOT NULL UNIQUE,
            package TEXT NOT NULL,
            monthly_bill REAL DEFAULT 0,
            status TEXT DEFAULT 'Active'
        )
    """)

    # Add sample data only if table is empty
    count = conn.execute(
        "SELECT COUNT(*) FROM customers"
    ).fetchone()[0]

    if count == 0:
        sample_data = [
            ("Kamal Perera", "0711234567", "Unlimited Plus", 2990, "Active"),
            ("Nimal Silva", "0772345678", "5G Max", 3990, "Active"),
            ("Saman Fernando", "0763456789", "Smart 1499", 1499, "Active"),
            ("Amal Jayasinghe", "0754567890", "Unlimited Plus", 2990, "Inactive"),
            ("Ruwan Bandara", "0785678901", "5G Max", 3990, "Active")
        ]

        conn.executemany("""
            INSERT INTO customers
            (name, mobile, package, monthly_bill, status)
            VALUES (?, ?, ?, ?, ?)
        """, sample_data)

    conn.commit()
    conn.close()


@app.route("/")
def index():

    conn = get_db()

    total_customers = conn.execute(
        "SELECT COUNT(*) FROM customers"
    ).fetchone()[0]

    active_customers = conn.execute(
        "SELECT COUNT(*) FROM customers WHERE status='Active'"
    ).fetchone()[0]

    monthly_revenue = conn.execute(
        "SELECT SUM(monthly_bill) FROM customers WHERE status='Active'"
    ).fetchone()[0] or 0

    customers = conn.execute(
        "SELECT * FROM customers ORDER BY id DESC LIMIT 5"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        total_customers=total_customers,
        active_customers=active_customers,
        monthly_revenue=monthly_revenue,
        customers=customers
    )


@app.route("/customers")
def customers():

    search = request.args.get("search", "")

    conn = get_db()

    if search:
        customers = conn.execute("""
            SELECT * FROM customers
            WHERE name LIKE ?
               OR mobile LIKE ?
               OR package LIKE ?
        """, (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        )).fetchall()
    else:
        customers = conn.execute(
            "SELECT * FROM customers ORDER BY id DESC"
        ).fetchall()

    conn.close()

    return render_template(
        "customers.html",
        customers=customers,
        search=search
    )


@app.route("/customer/<int:customer_id>")
def customer(customer_id):

    conn = get_db()

    customer = conn.execute(
        "SELECT * FROM customers WHERE id=?",
        (customer_id,)
    ).fetchone()

    conn.close()

    if customer is None:
        return "Customer not found", 404

    return render_template(
        "customer.html",
        customer=customer
    )


@app.route("/add", methods=["POST"])
def add_customer():

    name = request.form["name"]
    mobile = request.form["mobile"]
    package = request.form["package"]
    bill = request.form["bill"]

    conn = get_db()

    try:
        conn.execute("""
            INSERT INTO customers
            (name, mobile, package, monthly_bill)
            VALUES (?, ?, ?, ?)
        """, (name, mobile, package, bill))

        conn.commit()

    except sqlite3.IntegrityError:
        return "Mobile number already exists."

    finally:
        conn.close()

    return redirect(url_for("customers"))


@app.route("/api/customers")
def api_customers():

    conn = get_db()

    customers = conn.execute(
        "SELECT * FROM customers"
    ).fetchall()

    conn.close()

    return jsonify([
        dict(customer)
        for customer in customers
    ])


if __name__ == "__main__":
    init_db()

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
