from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("question/", views.QuestionList.as_view(), name="questions"),
    path("question/<slug:slug>", views.QuestionDetail.as_view(), name="question"),
    path("topic/<slug:slug>", views.TopicDetail.as_view(), name="topic"),
    path("page/<slug:slug>", views.PageDetail.as_view(), name="page"),
]
