from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    priority = models.IntegerField(default=0)
    parent = models.ForeignKey(
        "self", blank=True, null=True, related_name="children", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "slug",
            "parent",
        )
        verbose_name_plural = "topics"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        full_path = [self.name]
        p = self.parent
        while p is not None:
            full_path.append(p.name)
            p = p.parent
        return " -> ".join(full_path[::-1])


class Rating(models.Model):
    value = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.value)


class Question(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = HTMLField()
    ratings = models.ManyToManyField(Rating, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class Answer(models.Model):
    content = HTMLField()
    is_best_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ratings = models.ManyToManyField(Rating, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
