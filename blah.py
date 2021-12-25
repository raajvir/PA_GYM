# @app.route("/edit/<id_slug>", methods=["GET", "POST"])
# def edit(id_slug):
#     """Editing product info"""
#     if request.method == 'GET':
#         row = db.execute(
#             "SELECT * FROM products WHERE productid = :id", id=id_slug)
#         print('asdfasdfasdfadsf', id_slug)

#         outList = []
#         outList.append(list((row[0]).values()))
#         return render_template('edit.html', product=outList[0])
#         # return render_template("edit.html")
#     else:
#         rowx = db.execute(
#             "SELECT * FROM products WHERE productid = :id", id=id_slug)
#         print(rowx)
#         try:
#             units = int(request.form.get("units"))
#         except:
#             units = rowx.get('units')
#         try:
#             location = int(request.form.get("location"))
#         except:
#             location = rowx.get('location')
#         try:
#             p_name = int(request.form.get("p_name"))
#         except:
#             p_name = rowx.get('p_name')
#         try:
#             seller_name = int(request.form.get("seller_name"))
#         except:
#             seller_name = rowx.get('seller_name')
#         try:
#             seller_phone = int(request.form.get("seller_phone"))
#         except:
#             seller_phone = rowx.get('seller_phone')
#         try:
#             seller_email = int(request.form.get("seller_email"))
#         except:
#             seller_email = rowx.get('seller_email')

#         nxtime = time.time()

#         print(p_name, seller_name, units, seller_email,
#               location, id_slug, seller_phone, nxtime)
#         db.execute("UPDATE products SET p_name = :p_name, seller_name = :seller_name, units = :units, seller_phone = :seller_phone, seller_email = :seller_email, location = :location, time = :time WHERE productid = :prodid",
#                    p_name=p_name, seller_name=seller_name, units=units, seller_email=seller_email, location=location, seller_phone=seller_phone, time=nxtime, prodid=id_slug)
#         # db.execute("UPDATE products SET units = :units WHERE productid = :prodid", units=units, prodid=prodid)
#         return render_template('index.html')
import time

ntime = time.ctime(time.time())
ntime = ntime[4:]
ntime = ntime[0:6] + "," + ntime[15:]

print(ntime)
