from django.contrib import admin
from .models import Topic, Question, Answer, Rating, Page

# Register your models here.
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Rating)
admin.site.register(Page)
