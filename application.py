from flask import Flask, render_template
from db_utils import DBH
application = Flask(__name__)

@application.route("/")
def store():
    dbh = DBH();
    products = dbh.get_products();
    
    return render_template("store.html", products=products);

if __name__ == "__main__":
    application.run(debug=True, use_reloader=True, threaded=True)