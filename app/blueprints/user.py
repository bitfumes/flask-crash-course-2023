from app import User
from flask import Blueprint, redirect, render_template, request, url_for

bp = Blueprint("user", __name__)


@bp.route("/user/", methods=["GET", "POST"])
def user():
    if request.method == "POST":
        # store user in db
        return redirect(url_for("user.create"))
    else:
        users = User.query.all()
        return render_template("user/index.html", users=users)


@bp.route("/user/create")
def create():
    return render_template("user/create.html")


@bp.route("/user/<int:id>", methods=["DELETE", "PUT"])
def user_id(id):
    if request.method == "DELETE":
        return "<h1>Delete User!</h1>"
    elif request.method == "PUT":
        return "<h1>Update User!</h1>"


@bp.route("/user/<int:id>")
def about(id):
    return render_template("user/show.html", id=id)
    return render_template("user/show.html", id=id)
