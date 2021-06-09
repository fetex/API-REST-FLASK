from app.__init__ import db
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)
from flask_login import (
    logout_user,
    login_user,
    login_required,
)
from Flask.project.models.Client import Client
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    user = request.form.get("user")
    password = request.form.get("password")

    user = Client.query.filter_by(user=user).first()

    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again")
        return redirect(url_for("auth.login"))

    login_user(user)
    return redirect(url_for("main.profile"))


@auth.route("/signup", methods=["POST"])
def signup():
    email = request.form.get("email")

    user = Client.query.filter_by(email=email).first()

    if user:
        flash("Email address already exists")
        return redirect(url_for("auth.signup"))

    new_user = Client(
        email=email,
        user=request.form.get["user"],
        telephone=request.form.get["telephone"],
        name=request.form.get["name"],
        password=generate_password_hash(request.form.get["password"], method="sha256"),
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
