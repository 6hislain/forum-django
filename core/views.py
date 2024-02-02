from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
