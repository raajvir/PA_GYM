import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import time
from helpers import apology

# Configure application
app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["IMAGE_UPLOADS"] = "static/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
""" app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
"""

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///products.db")


@app.route("/")
# @login_required
def index():
    """Shows available goods"""
    rows = db.execute("SELECT * FROM products")
    # print(rows)
    # print(str(rows[0]))
    # x = list(rows[0])
    # y = list(x[0])
    # print(str(y))
    res = list((rows[0]).values())[0]
    print(res)

    iter = 0
    outList = []
    for dict in rows:
        outList.append(list(dict.values()))
        # print(list(dict.values())[8])

    return render_template("index.html", products=outList)

# @app.route("/post/<string:post_slug>", methods=['GET'])
# def post_route(post_slug):
#     post = Posts.query.filter_by(slug=post_slug).first()
#     return render_template('post.html', params=params, post=post


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        nonelist = []
        return render_template('search.html', rows=nonelist)
    else:
        # print("Asdfasdfasdfasdfakjl23o4u123lo4iu oirh12348729p8471234\n\nn\\nn\\n\n\n")
        query = request.form.get("query")
        # print(query)
        rows = db.execute(
            "SELECT * FROM products WHERE p_name LIKE '%'||?||'%'", (query))
        print(rows)
        print(rows[0])
        res = list((rows[0]).values())[0]
        print(res)

        iter = 0
        outList = []
        for dict in rows:
            outList.append(list(dict.values()))
        print(outList)
        return render_template("search.html", products=outList)


@app.route("/edit/<int:id_slug>", methods=["GET", "POST"])
def edit(id_slug):
    """Editing product info"""
    if request.method == 'GET':
        row = db.execute(
            "SELECT * FROM products WHERE productid = :id", id=id_slug)
        print('asdfasdfasdfadsf', id_slug)

        outList = []
        outList.append(list((row[0]).values()))
        return render_template('edit.html', product=outList[0], id_slug=id_slug)
        # return render_template("edit.html")
    else:
        print("Asdfasdfasdfasdfakjl23o4u123lo4iu oirh12348729p8471234\n\nn\\nn\\n\n\n")
        rowx = db.execute(
            "SELECT * FROM products WHERE productid = :id", id=id_slug)
        print(rowx)
        try:
            units = int(request.form.get("units"))
        except:
            units = rowx.get('units')
        try:
            location = str(request.form.get("location"))
        except:
            location = rowx.get('location')
        try:
            p_name = str(request.form.get("p_name"))
        except:
            p_name = rowx.get('p_name')
        try:
            seller_name = str(request.form.get("seller_name"))
        except:
            seller_name = rowx.get('seller_name')
        try:
            seller_phone = str(request.form.get("seller_phone"))
        except:
            seller_phone = rowx.get('seller_phone')
        try:
            seller_email = str(request.form.get("seller_email"))
        except:
            seller_email = rowx.get('seller_email')
        print("asdfa;sdlfkjas;dlkfja;dlfjas;ldfkja;lf")
        nxtime = time.ctime(time.time())
        nxtime = nxtime[4:]
        nxtime = nxtime[0:6] + "," + nxtime[15:]

        print(p_name, seller_name, units, seller_email,
              location, id_slug, seller_phone, nxtime)
        db.execute("UPDATE products SET p_name = :p_name, seller_name = :seller_name, units = :units, seller_phone = :seller_phone, seller_email = :seller_email, location = :location, time = :time WHERE productid = :prodid",
                   p_name=p_name, seller_name=seller_name, units=units, seller_email=seller_email, location=location, seller_phone=seller_phone, time=nxtime, prodid=id_slug)
        # db.execute("UPDATE products SET units = :units WHERE productid = :prodid", units=units, prodid=prodid)
        return redirect("/")


@app.route("/add", methods=["GET", "POST"])
def add():
    """Adding new product"""
    if request.method == 'GET':
        return render_template("add.html")
    else:
        ntime = time.ctime(time.time())
        ntime = ntime[4:]
        ntime = ntime[0:6] + "," + ntime[15:]
        img_src = 'static/uploads\istockphoto-1128826884-170667a.jpg'
        if request.files["img"] != None:
            image = request.files["img"]
            print(image)
            img_src = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)
            print(img_src)
            image.save(img_src)

            print("Image saved")

        # img_src = img_src.replace("uploads\", "uploads/")
        p_name = str(request.form.get("p_name"))
        seller_name = str(request.form.get("seller_name"))
        print(request.form.get('units'))
        units = int(request.form.get("units"))
        seller_phone = (request.form.get("seller_phone"))
        seller_email = str(request.form.get("seller_email"))
        location = str(request.form.get("location"))
        # product_desc = str(request.form.get("product_desc"))

        # add time remove product desc in db
        db.execute("INSERT INTO products(p_name,seller_name,units,seller_phone,seller_email, location, time, img_src) VALUES (:p_name, :seller_name, :units,:seller_phone, :seller_email,:location, :time, :img_src)",
                   p_name=p_name, seller_name=seller_name, units=units, seller_email=seller_email, location=location, seller_phone=seller_phone, time=ntime, img_src=img_src)

        return redirect("/")


def allowed_image(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == "__main__":
    app.run()
