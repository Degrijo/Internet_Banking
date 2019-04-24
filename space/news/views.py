from django.views.generic import ListView, DetailView
from news.models import Article


class ArticleListView(ListView):
    template_name = "news/posts.html"
    queryset = Article.objects.all().order_by("-date")[:20]
    context_object_name = "article_list"


class ArticleDetailView(DetailView):
    template_name = "news/post.html"
    model = Article
    context_object_name = "article_view"
