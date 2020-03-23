from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import TemplateView
from journal.models import Post

class PostFeed(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = dict()
        context["posts"] = Post.objects.all()
        return context