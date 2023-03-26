from flask import Flask, render_template, redirect
from db_utils import DBH
application = Flask(__name__)

@application.route("/")
def store():
    dbh = DBH();
    products = dbh.get_all_products();
    
    return render_template("store.html", products=products);

@application.route("/product/<int:product_id>")
def product_page(product_id):
    dbh = DBH();
    product = dbh.get_product(product_id);
    if (product != None):
        return render_template("product.html", product=product);
    else:
        return redirect("/error");

#for if a page is not found
@application.route("/error")
def error_page():
    return render_template("error.html");

if __name__ == "__main__":
    application.run(debug=True, use_reloader=True, threaded=True)