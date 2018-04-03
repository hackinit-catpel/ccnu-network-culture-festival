# coding: utf-8

"""
    admin site

    use: Flask-Admin
    -- https://flask-admin.readthedocs.org/en/latest/

"""

# import flask_login as login
# import flask_admin as admin
# from flask_login import current_user
# from flask_admin import Admin, BaseView, expose
# from flask_admin.contrib.sqla import ModelView
# from app import app, db
# from app.models import AnonymousUser
# from flask import redirect, flash, url_for
#
#
# class MyAdminIndexView(admin.AdminIndexView):
#     def is_accessible(self):
#         return login.current_user.is_admin()
#
#     def inaccessible_callback(self, name, **kwargs):
#         return redirect(url_for('auth.login'))
#
#
# admin = Admin(
#     app,
#     name="admin site",
#     template_mode="bootstrap3",
#     index_view=MyAdminIndexView(),
#     base_template='admin/logout.html'
# )
#
#
# # sql models management
# from app.models import User
# admin.add_view(ModelView(User, db.session))
#
# from app.models import Role
# admin.add_view(ModelView(Role, db.session))
#
# from app.models import Movie
# admin.add_view(ModelView(Movie, db.session))
#
# from app.models import Anime
# admin.add_view(ModelView(Anime, db.session))
#
# from app.models import Course
# admin.add_view(ModelView(Course, db.session))
#
# from app.models import Photo
# admin.add_view(ModelView(Photo, db.session))
#
# from app.models import Article
# admin.add_view(ModelView(Article, db.session))
#
# from app.models import Startup
# admin.add_view(ModelView(Startup, db.session))

# from app.models import W_Startup
# admin.add_view(ModelView(W_Startup, db.session))
#
# from app.models import W_Movie
# admin.add_view(ModelView(W_Movie, db.session))
#
# from app.models import W_Anime
# admin.add_view(ModelView(W_Anime, db.session))
#
# from app.models import W_Course
# admin.add_view(ModelView(W_Course, db.session))
#
# from app.models import W_Photo
# admin.add_view(ModelView(W_Photo, db.session))
#
# from app.models import W_Article
# admin.add_view(ModelView(W_Article, db.session))
#
# from app.models import Notice
# admin.add_view(ModelView(Notice, db.session))


from . import admin
from flask import render_template, url_for, redirect, flash
from app.models import Anime,Article,User,Role,Movie,Course,Notice,Photo,Startup

@admin.route('/')
def index():
    return render_template("admin/home.html")

@admin.route("/user/")
def user_manage():
    return render_template("admin/user.html")


@admin.route("/movie/")
def movie_manage():
    return render_template("admin/movie.html")

@admin.route("/anime/")
def anime_manage():
    return render_template("admin/anime.html")

@admin.route("/course/")
def course_manage():
    return render_template("admin/course.html")

@admin.route("/photo/")
def photo_manage():
    return render_template("admin/photo.html")

@admin.route("/article/")
def article_manage():
    return render_template("admin/article.html")

@admin.route("/startup/")
def startup_manage():
    return render_template("admin/startup.html")
