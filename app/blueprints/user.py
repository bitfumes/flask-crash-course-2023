from flask import Blueprint, render_template, request

bp = Blueprint("user", __name__)


@bp.route("/user/", methods=["GET", "POST"])
def user():
    if request.method == "POST":
        return "<h1>Create new User!</h1>"
    else:
        return render_template("user/index.html")


@bp.route("/user/<int:id>", methods=["DELETE", "PUT"])
def user_id(id):
    if request.method == "DELETE":
        return "<h1>Delete User!</h1>"
    elif request.method == "PUT":
        return "<h1>Update User!</h1>"


@bp.route("/user/<int:id>")
def about(id):
    return f"<h1>Welcome {id} </h1>"
