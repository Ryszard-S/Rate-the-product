from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .extenctions import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))


@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        nick = request.form.get('nick')
        first_name = request.form.get("firstName")
        passw1 = request.form.get("password1")
        passw2 = request.form.get("password2")
        data = request.form

        if len(email) < 4:
            flash("Email must be grater than 3 characters.", category='error')
        elif len(first_name) < 2:
            flash("Email must be grater than 1 characters.", category='error')
        elif passw1 != passw2:
            flash("Passwords don\'t match.", category='error')
        elif len(passw1) < 1:
            flash("Email must be at least 7 characters.", category='error')
        else:
            # add user to database
            passwd = generate_password_hash(passw1, method="sha256")
            new_user = User(email=email, name=first_name, nick=nick, password=passwd)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created.", category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html", user=current_user)
