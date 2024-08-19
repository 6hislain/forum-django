from django.contrib.auth import authenticate, login as login_me_in, logout as log_me_out
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_http_methods
from .models import Question, Answer, Topic, Page


# Create your views here.
def home(request):
    pages = Page.objects.all()
    topics = Topic.objects.all()
    questions = Question.objects.order_by("-id")
    paginator = Paginator(questions, 50)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    return render(
        request,
        "home.html",
        {"pages": pages, "topics": topics, "page_object": page_object},
    )


class QuestionList(ListView):
    paginate_by = 48
    queryset = Question.objects.order_by("-created_at")
    template_name = "question/index.html"


class QuestionDetail(DetailView):
    model = Question
    paginate_by = 48
    template_name = "question/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        question = self.get_object()
        answers = Answer.object.filter(question=question).order_by("-created_at")

        paginator = Paginator(answers, self.paginate_by)
        page = self.request.GET.get("page")

        try:
            paginated_answers = paginator.page(page)
        except PageNotAnInteger:
            paginated_answers = paginator.page(1)
        except EmptyPage:
            paginated_answers = paginator.page(paginator.num_pages)

        context["answers"] = paginated_answers

        return context


class PageDetail(DetailView):
    model = Page
    template_name = "page/detail.html"


class TopicDetail(DetailView):
    model = Topic
    paginate_by = 48
    template_name = "topic/detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        topic = self.get_object()
        questions = Question.object.filter(topic=topic).order_by("-created_at")

        paginator = Paginator(questions, self.paginate_by)
        page = self.request.GET.get("page")

        try:
            paginated_questions = paginator.page(page)
        except PageNotAnInteger:
            paginated_questions = paginator.page(1)
        except EmptyPage:
            paginated_questions = paginator.page(paginator.num_pages)

        context["questions"] = paginated_questions

        return context


@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    elif request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == "" or password != confirm_password:
            messages.info(request, "Password do not match")
            return redirect("register")

        if email == "" or User.objects.filter(email=email).exists():
            messages.info(request, "Email already taken")
            return redirect("register")

        if username == "" or User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return redirect("register")

        new_user = User.objects.create_user(
            username=username, email=email, password=password
        )
        new_user.save()

        user_login = authenticate(username=username, password=password)
        login_me_in(request, user_login)

        return redirect("home")


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Invalid credentials")
            return redirect("login")

        login_me_in(request, user)
        return redirect("home")


@login_required(login_url="login")
def logout(request):
    log_me_out(request)
    return redirect("home")
