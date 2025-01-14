from flask import Blueprint, render_template
from flask_login import login_required
from app.services.user import UserService
from flask import Blueprint, render_template, redirect, url_for
from flask_injector import inject

admin_view = Blueprint("admin_view", __name__)

@admin_view.route("/profile")
@login_required
def profile():
    return render_template("/admin_view/profile.html")




