from flask import Flask, render_template, redirect, request, jsonify, session
from db_utils import DBH
import util
import secrets

application = Flask(__name__)
application.secret_key = secrets.token_urlsafe(16)

@application.context_processor
def utility_processor():
    def img_url_trim(url):
        dirs = url.split("\\");
        trimmed_url = '/'.join(dirs[1:4]);
        return trimmed_url
    return dict(img_url_trim=img_url_trim)


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

@application.route("/cart")
def showCart():
    #returns a LIST of DICTS representing the db row PLUS: TOTAL and order QTTY
    cart_info = util.get_cart_info(session.get("cart")) 
    
    return render_template("cart.html", cart=cart_info);

@application.route("/addToCart", methods=["POST"])
def add_to_cart():
    if (session.get("cart") == None):
        session["cart"] = {}
    
    if request.method == "POST":
        desc_data = request.get_json()
        
        name = desc_data["product_name"]
        id = str(desc_data["product_id"])
        qtty = int(desc_data["product_qtty"])
        
        cart = session["cart"]
        if id not in cart:
            cart[id] = qtty
        else:
            cart[id] += qtty;
        
        #save cart back in our session
        session["cart"] = cart
        print("cur cart: " , cart);
    results = {'updated': 'true'}
    return jsonify(results);

if __name__ == "__main__":
    application.run(debug=True, use_reloader=True, threaded=True)