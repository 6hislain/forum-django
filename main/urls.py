from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("register", views.register, name="register"),
    path("question/", views.QuestionList.as_view(), name="questions"),
    path("question/<slug:slug>", views.QuestionDetail.as_view(), name="question"),
    path("topic/<slug:slug>", views.TopicDetail.as_view(), name="topic"),
    path("page/<slug:slug>", views.PageDetail.as_view(), name="page"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path(
        "contact/", TemplateView.as_view(template_name="contact.html"), name="contact"
    ),
    path(
        "license/", TemplateView.as_view(template_name="license.html"), name="license"
    ),
]
