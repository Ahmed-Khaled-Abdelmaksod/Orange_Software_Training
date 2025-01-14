import uuid
from flask import Blueprint, render_template, redirect, url_for
from flask_injector import inject
from app.services.user import UserService
from flask_login import login_required
from app.forms.auth.login_form import LoginForm
from app.forms.auth.signup_form import SignupForm

from werkzeug.security import generate_password_hash
auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
@inject
def login(user_service: UserService):
    login_form = LoginForm()

    error_message = ""

    if login_form.validate_on_submit():
        if user_service.login(login_form.email.data, login_form.password.data):
            if user_service.is_admin(login_form.email.data):
                return redirect(url_for("admin_view.profile"))
            else:
                return redirect(url_for("user.profile"))

        error_message = "incorrect email or password"

    return render_template("/auth/login.html", form=login_form, error_message=error_message)

@auth.route("/signup", methods=["GET", "POST"])
@inject
def signup(user_service: UserService):
    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        if not user_service.get_by_email(email=signup_form.email.data):
            user_service.signup(
                signup_form.name.data,
                signup_form.email.data,
                signup_form.password.data,
            )

        return redirect(url_for("auth.login"))

    return render_template("/auth/signup.html", form=signup_form)

@auth.route("/logout")
@login_required
@inject
def logout(user_service: UserService):
    user_service.logout()
    return redirect(url_for("dashboard.home"))

# @auth.route("/test")
# @inject
# def inject_admin(user_service: UserService):

#     user_service.insert_user(2000,str(uuid.uuid4()),"Moh123456","AhmedKhaled",generate_password_hash("Ahmed123"),"Admin")
#     return "Admin inserted !!"