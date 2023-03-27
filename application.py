from flask import Flask, render_template, redirect, request, jsonify
from db_utils import DBH
application = Flask(__name__)

@application.context_processor
def utility_processor():
    def jinja_img_url_trim(url):
        dirs = url.split("\\");
        trimmed_url = '/'.join(dirs[1:4]);
        return trimmed_url
    return dict(jinja_img_url_trim=jinja_img_url_trim)


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

@application.route("/addToCart", methods=["POST"])
def add_to_cart():
    if request.method == "POST":
        desc_data = request.get_json()
        product_name = desc_data["product_name"]
        product_id = desc_data["product_id"]
        print("adding " , product_id , " to cart " , product_name);
    results = {'updated': 'true'}
    return jsonify(results);

if __name__ == "__main__":
    application.run(debug=True, use_reloader=True, threaded=True)