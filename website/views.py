import io
import uuid
from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, current_app, url_for, abort
from flask_login import current_user, login_required
from sqlalchemy import or_

from .extenctions import db
from .models import Products, Brand, Comments, ProductPhotos, User
from filestack import Client

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)


@views.route("/my_products", methods=['GET', 'POST'])
@login_required
def my_products():
    page = request.args.get('page', 1, type=int)
    products = Products.query.filter_by(id_user=current_user.get_id()).join(Brand,
                                                                            Products.id_brand == Brand.id).add_columns(
        Products.name, Products.description, Brand.name).paginate(page=page, per_page=12)

    return render_template("my_products.html", user=current_user, products=products, page=page)


@views.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():
    brands = Brand.query.all()
    if request.method == 'POST':
        name_product = request.form.get('name')
        brand = request.form.get('brand')
        description = request.form.get('description')
        barcode = request.form.get('barcode')
        image = request.files['upload']

        product = Products(name=name_product, id_brand=brand, description=description, id_user=current_user.get_id(),
                           barcode=barcode)
        db.session.add(product)
        db.session.commit()

        if image:
            if image.filename == '':
                flash('Choose file', 'error')
                return redirect(request.url)

            elif not allowed_file(image.filename):
                flash("Bad filename extencions!", 'error')
                return redirect(request.url)

            else:

                ext = image.mimetype.split('/')[1]
                name = str(uuid.uuid4())
                filename = name + "." + ext
                store_params = {
                    "filename": filename,
                    "mimetype": image.mimetype
                }
                client = Client(current_app.config['IMAGE_UPLOAD_API'])
                file = client.upload(file_obj=io.BytesIO(image.read()), store_params=store_params)
                photo = ProductPhotos(id_user=current_user.get_id(), id_product=product.id, photo=file.url,
                                      file_name=filename)
                product.photo = file.url
                db.session.add(photo, product)

                db.session.commit()
                flash("Product added", 'message')

        else:
            db.session.add(product)
            db.session.commit()
            flash("Product added without photo", 'message')

    return render_template("upload.html", brands=brands)


@views.route("/search", methods=['GET'])
def search():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 12, type=int)
    sort = request.args.get('sort')
    sub = None
    if sort == 'rate_asc':
        sub = Products.rating.asc()
    elif sort == 'rate_desc':
        sub = Products.rating.desc()
    elif sort == 'alfa_asc':
        sub = Products.name.asc()
    elif sort == 'alfa_desc':
        sub = Products.name.desc()
    elif sort == 'date_asc':
        sub = Products.date.asc()
    elif sort == 'date_desc':
        sub = Products.date.desc()

    product = db.session.query(Brand.name,
                               Products.name,
                               Products.id,
                               Products.rating,
                               Products.photo
                               ).select_from(Products).join(Brand).filter(
        or_(Products.name.ilike(f'%{query}%'), Products.description.ilike(f'%{query}%'))).order_by(sub).paginate(
        page=page, per_page=per_page)

    return render_template("search.html", products=product, page=page, query=query,
                           per_page=per_page, sort=sort)


@views.route('/product/<int:id_product>', methods=["GET", "POST"])
def product(id_product):
    product = Products.query.filter_by(id=id_product).join(Brand, Products.id_brand == Brand.id).add_columns(
        Brand.name,
        Products.id).first_or_404()

    comments = Comments.query.filter_by(id_product=id_product).join(User, Comments.id_user == User.id).add_columns(
        User.nick).all()

    photos = ProductPhotos.query.filter_by(id_product=id_product).all()

    comment_added = False
    if current_user.is_authenticated:
        x = Comments.query.filter_by(id_user=current_user.get_id(), id_product=id_product).all()
        if x:
            comment_added = True

    if request.method == "POST" and not comment_added:
        stars = request.form.get("rate")
        comment = request.form.get("comment")
        if stars and comment:
            new_comment = Comments(id_user=current_user.get_id(),
                                   id_product=id_product,
                                   comment=comment,
                                   rating=stars)
            db.session.add(new_comment)
            db.session.commit()
        else:
            flash('Wypełnij obowiązkowe pola', 'error')
        return redirect(url_for("views.product", id_product=id_product))

    return render_template("product.html", user=current_user, product=product, comments=comments,
                           comment_added=comment_added, photos=photos, str=str)


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
@login_required
def user(id_user):
    if current_user.is_authenticated and current_user.get_id() == str(id_user):
        info: User = User.query.filter_by(id=id_user).first_or_404()
        dni = (datetime.now() - info.data_rejestracji).days
        products_added = db.session.query(Products.photo, Brand.name, Products.name, Products.date).join(Brand).filter(
            Products.id_user == id_user)
    else:
        abort(403)
    return render_template("user.html", user=current_user, info=info, czas=dni, products=products_added)


def allowed_file(filename):
    if not '.' in filename:
        return False

    ext = filename.rsplit('.')[-1]

    if ext.lower() in current_app.config['IMAGE_EXTENSIONS']:
        return True
    else:
        return False
