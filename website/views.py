import os
import uuid

from flask import Blueprint, render_template, request, flash, redirect, current_app, url_for
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from datetime import datetime

from .extenctions import db
from .models import Products, Brand, Comments, Login

views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)


@views.route("/my_products", methods=['GET', 'POST'])
@login_required
def my_products():
    page = request.args.get('page', 1, type=int)
    prod = Products.query.filter_by(id_user=current_user.get_id()).paginate(page=page, per_page=12)
    prodd = Products.query.filter_by(id_user=current_user.get_id()).join(Brand, Products.brand == Brand.id).add_columns(
        Products.name, Products.description,
        Brand.name).paginate(page=page,
                             per_page=12)
    proddd = Products.query.join(Brand, Products.brand == Brand.id).add_columns(Products.name, Products.description,
                                                                                Brand.name)


    return render_template("my_products.html", user=current_user, products=prodd, page=page)


@views.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():
    brands = Brand.query.all()
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
        if request.files:
            image = request.files['image']
            name_product = request.form.get('name')
            brand = request.form.get('brand')
            description = request.form.get('description')
            barcode = request.form.get('barcode')
            if image.filename == '':
                flash('Choose file', 'error')
                return redirect(request.url)

            if not allowed_file(image.filename):
                flash("Bad filename extencions!", 'error')
                return redirect(request.url)

            else:
                filename = secure_filename(image.filename)
                ext = image.content_type.split('/')[1]
                name = str(uuid.uuid4())
                filename = name + "." + ext
                image.save(os.path.join(current_app.config['IMAGE_UPLOADS'], filename))
                product = Products(name=name_product, brand=brand, description=description, photo=filename,
                                   barcode=barcode, id_user=current_user.get_id())
                db.session.add(product)
                db.session.commit()
                flash("Product added", 'message')

    return render_template("upload.html", user=current_user, brands=brands)


@views.route("/search", methods=['GET', 'POST'])
def search():
    q = request.args.get('q')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 12, type=int)

    if q:
        product = Products.query.join(Brand, Products.brand == Brand.id).add_columns(Brand.name, Products.name,
                                                                                     Products.photo,
                                                                                     Products.id,
                                                                                     Products.rating).filter(
            Products.name.contains(q)).paginate(
            page=page, per_page=per_page)
    else:

        product = Products.query.join(Brand, Products.brand == Brand.id).add_columns(Brand.name, Products.name,
                                                                                     Products.photo,
                                                                                     Products.id,
                                                                                     Products.rating).paginate(
            page=page, per_page=per_page)
    return render_template("search.html", products=product, user=current_user, page=page, q=q, per_page=per_page)


@views.route('/product/<int:id_product>', methods=["GET", "POST"])
def product(id_product):
    product = Products.query.filter_by(id=id_product).join(Brand, Products.brand == Brand.id).add_columns(Products.name,
                                                                                                          Products.rating,
                                                                                                          Products.date,
                                                                                                          Products.photo,
                                                                                                          Products.description,
                                                                                                          Products.barcode,
                                                                                                          Brand.name,
                                                                                                          Products.id).first_or_404()

    comments = Comments.query.filter_by(id_product=id_product).join(Login, Comments.id_user == Login.id).add_columns(
        Login.nick,
        Comments.comment,
        Comments.rating,
        Comments.date,
        Comments.id,
        Comments.id_user)

    comment_added = False
    if current_user.is_authenticated:
        x = Comments.query.filter_by(id_user=current_user.get_id(), id_product=id_product).all()
        if x:
            comment_added = True

    if request.method == "POST" and not comment_added:
        stars = request.form.get("stars")
        comment = request.form.get("comment")
        comm = Comments(id_user=current_user.get_id(),
                        id_product=id_product,
                        comment=comment,
                        rating=stars)
        db.session.add(comm)
        db.session.commit()
        return redirect(url_for("views.product", id_product=id_product))

    return render_template("product.html", user=current_user, product=product, comments=comments,
                           comment_added=comment_added, str=str)


@views.route("/delete/<int:id_comment>/<int:id_user>/<int:id_product>", methods=["GET", "POST"])
def delete(id_user, id_comment, id_product):
    if current_user.is_authenticated and current_user.get_id() == str(id_user):
        x = Comments.query.filter(Comments.id == id_comment and Comments.id_user == id_user).first_or_404()
        if x:
            db.session.delete(x)
            db.session.commit()
            flash("Komentarz usunięty", category="message")
            return redirect(url_for("views.product", id_product=id_product))

    return render_template("home.html", user=current_user)


@views.route("/user/<string:id_user>", methods=["GET", "POST"])
def user(id_user):
    if current_user.is_authenticated and id_user == current_user.get_id():
        x: Login = Login.query.filter_by(id=id_user).first_or_404()
        dni = (datetime.now() - x.data_rejestracji).days
    return render_template("user.html", user=current_user, info=x, czas=dni)


def allowed_file(filename):
    if not '.' in filename:
        return False

    ext = filename.rsplit('.', 1)[1]

    if ext.upper() in current_app.config['ALLOWED_FILE_EXTENTIONS']:
        return True
    else:
        return False
