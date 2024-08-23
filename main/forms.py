from django import forms
from .models import Topic, Question, Rating, Answer, Page


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = "__all__"


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = "__all__"
