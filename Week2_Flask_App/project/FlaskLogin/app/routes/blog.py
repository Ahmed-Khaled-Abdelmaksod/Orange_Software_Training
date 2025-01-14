import uuid
from flask import Blueprint, render_template
from flask_login import login_required
from app.services.blog import BlogService
from flask import Blueprint, render_template, redirect, url_for
from app.forms.auth.blogs.create_form import CreateForm
from app.forms.auth.blogs.edit_form import EditForm
from flask_injector import inject

blog = Blueprint("blog", __name__)

@blog.route("/")
@inject
def list_blogs(blog_service : BlogService):
    blogs = blog_service.get_all()
    return render_template("/blog/blogs.html",blogs=blogs)

@blog.route("/create")
def create():
    return render_template("/blog/create.html", form=CreateForm())

@blog.route("/", methods=["POST"])
@inject
def store(blog_service: BlogService):
    create_form = CreateForm()

    if create_form.validate_on_submit():
        blog_service.create(
            title=create_form.title.data,
            description=create_form.description.data,
            author_id=create_form.author_id.data,
            dislikes=0,
            likes=0,
            id=create_form.id.data
        )

        return redirect(url_for("blog.list_blogs"))

    return render_template("/blog/create.html", form=create_form)

@blog.route("/<id>")
@inject
def view(blog_service: BlogService, id):
    blog = blog_service.get_by_id(id)

    if not blog:
        return redirect(url_for("blog.list_blogs"))

    return render_template("blog/view.html", blog=blog)

@blog.route("/<id>/edit")
@inject
def edit(blog_Service: BlogService, id):
    blog = blog_Service.get_by_id(id)

    if not blog:
        return redirect(url_for("blog.list_blogs"))

    return render_template("blog/edit.html", form=EditForm(), blog=blog)

@blog.route("/<id>", methods=["POST"])
@inject
def update(blog_service: BlogService, id):
    product = blog_service.get_by_id(id)

    if not blog:
        return redirect(url_for("blog.list_blogs"))

    edit_form = EditForm()

    if edit_form.validate_on_submit():
        blog_service.update(
            blog,
            edit_form.title.data,
            edit_form.description.data
        )

        return redirect(url_for("blog.list_blogs"))

    return render_template("blog/view.html", blog=blog)

@blog.route("/<id>", methods=["DELETE"])
@inject
def delete(blog_Service: BlogService, id):
    blog = blog_Service.get_by_id(id)

    if blog:
        blog_Service.delete(blog)

    return redirect(url_for("blog.list_blogs"))
# @blog.route("/test")
# @inject
# def inject_blog(blog_service: BlogService):
#     blog_service.create(1,'FootBall','lorem lshfrohfs djtgdl',0,0,1)
#     return "blog inserted !!"