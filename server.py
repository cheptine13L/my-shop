from flask import Flask, render_template, request, redirect, session, url_for
import json, os
from datetime import datetime
from products import PRODUCTS

app = Flask(__name__)
app.secret_key = "microslop"

ORDERS_DIR = "submitted-orders"
os.makedirs(ORDERS_DIR, exist_ok=True)


def get_cart():
    return session.get("cart", {})


def save_cart(cart):
    session["cart"] = cart


@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)


@app.route("/cart")
def cart():
    cart = get_cart()
    items = []
    total = 0
    for pid, qty in cart.items():
        product = PRODUCTS.get(pid)
        if product:
            subtotal = product["price"] * qty
            total += subtotal
            items.append({"product": product, "qty": qty, "subtotal": subtotal})
    return render_template("cart.html", items=items, total=total)


@app.route("/cart/add-item")
def add_item():
    pid = request.args.get("id")
    if pid and pid in PRODUCTS:
        cart = get_cart()
        cart[pid] = cart.get(pid, 0) + 1
        save_cart(cart)
    return redirect(url_for("index"))


@app.route("/cart/remove-item")
def remove_item():
    pid = request.args.get("id")
    cart = get_cart()
    if pid in cart:
        del cart[pid]
        save_cart(cart)
    return redirect(url_for("cart"))


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = get_cart()
    items = []
    total = 0
    for pid, qty in cart.items():
        product = PRODUCTS.get(pid)
        if product:
            subtotal = product["price"] * qty
            total += subtotal
            items.append({"product": product, "qty": qty, "subtotal": subtotal})

    if request.method == "POST":
        order = {
            "full_name": request.form.get("full_name"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "address": request.form.get("address"),
            "payment_method": request.form.get("payment_method"),
            "items": [{"name": i["product"]["name"], "qty": i["qty"], "subtotal": i["subtotal"]} for i in items],
            "total": total,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # print in consola
        print("\n===== COMANDA NOUA =====")
        print(json.dumps(order, indent=2, ensure_ascii=False))
        print("========================\n")

        # salveaza in fisier
        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
        with open(os.path.join(ORDERS_DIR, filename), "w", encoding="utf-8") as f:
            json.dump(order, f, indent=2, ensure_ascii=False)

        session["cart"] = {}
        return render_template("order_success.html", order=order)

    return render_template("checkout.html", items=items, total=total)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
